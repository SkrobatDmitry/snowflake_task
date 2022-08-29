import pandas as pd
from datetime import datetime

from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeHook, SnowflakeOperator


def write_from_csv_to_raw():
    hook = SnowflakeHook(snowflake_conn_id='snowflake_conn')
    alch = hook.get_sqlalchemy_engine()

    df = pd.read_csv(Variable.get('ios_apps_csv_path'))
    df.to_sql('raw_table', con=alch, if_exists='append', index=False, chunksize=10000)


with DAG('snowflake_task',
         schedule_interval='@once',
         start_date=datetime(2022, 8, 26, 0, 0),
         template_searchpath=Variable.get('snowflake_searchpath'),
         catchup=False
         ) as dag:

    create_tables_task = SnowflakeOperator(
        task_id='create_tables',
        snowflake_conn_id='snowflake_conn',
        sql='create_tables.sql'
    )

    create_streams_task = SnowflakeOperator(
        task_id='create_streams',
        snowflake_conn_id='snowflake_conn',
        sql='create_streams.sql'
    )

    write_from_csv_to_raw_task = PythonOperator(
        task_id='write_from_csv_to_raw',
        python_callable=write_from_csv_to_raw
    )

    write_from_raw_to_stage_task = SnowflakeOperator(
        task_id='write_from_raw_to_stage',
        snowflake_conn_id='snowflake_conn',
        sql='write_from_raw_to_stage.sql'
    )

    write_from_stage_to_master_task = SnowflakeOperator(
        task_id='write_from_stage_to_master',
        snowflake_conn_id='snowflake_conn',
        sql='write_from_stage_to_master.sql'
    )

    create_tables_task >> create_streams_task >> \
    write_from_csv_to_raw_task >> write_from_raw_to_stage_task >> write_from_stage_to_master_task
