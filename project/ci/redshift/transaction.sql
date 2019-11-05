DROP TABLE transaction IF NOT EXISTS 

CREATE TABLE transaction (
    Group_Company_Code VARCHAR (10),
    Wireless_Sales_Slip_No integer,
    Column_No  VARCHAR (30),
    Product_Code VARCHAR (30),
    Full_Tank_Number  VARCHAR (30),
    Selling_Price integer, 
    Meter_No VARCHAR (30),
    Hot_Cold_Classification VARCHAR (30),
    Last_Visit_Inventory VARCHAR (30),
    Sales_Quantity integer,
    Sales_After_Supply integer,
    Product_Code_Before_Replacement VARCHAR (30),
    Full_Tank_Quantity_Before_Product_Replacement VARCHAR (30),
    Number_Of_Products_Introduced_Before_Product_Replacement integer,
    Price_Before_Replacement NUMERIC,
    Meter No. before product replacement VARCHAR (30),
    Hot_Cold_Classification_Before_Product_Replacement VARCHAR (30),
    Site_Code VARCHAR (30),
    Department_Code VARCHAR (30),
    Route_Code VARCHAR (30),
    Customer_Number integer,
    Branch_Number integer,
    Equipment_Code VARCHAR (30),
    Sales_Date timestamp,
    Last_Visit_Date timestamp,
    Last_Calibration_Date timestamp,
    Number_Of_Sales_Update_Failure integer,
    Buying_Place_Code VARCHAR (30),
    Sales system representative code VARCHAR (30),
    Sales method detail code VARCHAR (30),
    In_Out_Classification VARCHAR (30),
    Annual contribution sales capacity conversion NUMERIC,
    Open_Closed_Classification VARCHAR (30),
    Contents_Manufacturer_Code VARCHAR (30),
    Installation_Date VARCHAR (30),
    Number_Of_Adjacent_VM_CC NUMERIC,
    Number_Of_Adjacent_VM_K  NUMERIC,
    Number_Of_Adjacent_VM_A  NUMERIC,
    Number_Of_Adjacent_VM_DY NUMERIC,
    Number_Of_Adjacent_VM_IT NUMERIC,
    Number_Of_Adjacent_VM_PO NUMERIC,
    Number_Of_Adjacent_VM_OT NUMERIC,
    Number_Of_Adjacent_VM_SF NUMERIC
    ); 