DROP TABLE product IF EXISTS; 

CREATE TABLE product(
    Product_Code VARCHAR (30),
    Product_Type_Code  VARCHAR (30),
    Product_Classification_Code VARCHAR (30),
    Genre_Code VARCHAR (30),
    Kanji_Official_Name VARCHAR (50),
    Container_Capacity_Code VARCHAR (30),
    Hot_Cold_Classification VARCHAR (30),
    Release_Date timestamp
    );