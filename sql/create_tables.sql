CREATE OR REPLACE TABLE raw_table (
    "_ID"                               VARCHAR(8191),
    "IOS_App_Id"                        NUMBER(38, 0),
    "Title"                             VARCHAR(8191),
    "Developer_Name"                    VARCHAR(8191),
    "Developer_IOS_Id"                  FLOAT,
    "IOS_Store_Url"                     VARCHAR(8191),
    "Seller_Official_Website"           VARCHAR(8191),
    "Age_Rating"                        VARCHAR(8191),
    "Total_Average_Rating"              FLOAT,
    "Total_Number_of_Ratings"           FLOAT,
    "Average_Rating_For_Version"        FLOAT,
    "Number_of_Ratings_For_Version"     NUMBER(38, 0),
    "Original_Release_Date"             VARCHAR(8191),
    "Current_Version_Release_Date"      VARCHAR(8191),
    "Price_USD"                         FLOAT,
    "Primary_Genre"                     VARCHAR(8191),
    "All_Genres"                        VARCHAR(8191),
    "Languages"                         VARCHAR(8191),
    "Description"                       VARCHAR(8191)
);

CREATE OR REPLACE TABLE stage_table LIKE raw_table;
CREATE OR REPLACE TABLE master_table LIKE raw_table;