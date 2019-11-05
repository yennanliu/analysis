DROP TABLE vendor_machine IF EXISTS; 

CREATE TABLE vendor_machine(
      Organization_Group_Code VARCHAR (30),
      Equipment_Code VARCHAR (30),
      Customer_Number integer,
      Branch_Number integer,
      Model_Year integer,
      Number_Of_Cell integer,
      HOT_Selection_Number integer,
      Number_Of_Buttons integer,
      Number_Of_Column_Rows integer,
      Model_500_PET_Selection VARCHAR (30),
      Model_500_Cans_Selection VARCHAR (30),
      Installation_Date timestamp,
      Prefecture_Code VARCHAR (30),
      City_Code VARCHAR (30),
      Buying_Place_Code VARCHAR (30),
      In_Out_Classification VARCHAR (30),
      Open_Closed_Classification VARCHAR (30),
      Group_Company_Code VARCHAR (30),
      Column_No integer,
      Column_Position_(Row) integer,
      Column_Position_(Column) integer
      );