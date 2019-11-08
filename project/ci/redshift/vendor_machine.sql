DROP TABLE fc.vendor_machine IF EXISTS;

CREATE TABLE fc.vendor_machine ( 
    organization_group_code  VARCHAR (30), 
    equipment_code           VARCHAR (30), 
    customer_number          INTEGER, 
    branch_number            INTEGER, 
    model_year               INTEGER, 
    number_of_cell           INTEGER, 
    hot_selection_number     INTEGER, 
    number_of_buttons        INTEGER, 
    number_of_column_rows    INTEGER, 
    model_500_pet_selection  VARCHAR (30), 
    model_500_cans_selection VARCHAR (30), 
    installation_date        TIMESTAMP, 
    prefecture_code            VARCHAR (30), 
    city_code                  VARCHAR (30), 
    buying_place_code          VARCHAR (30), 
    in_out_classification      VARCHAR (30), 
    open_closed_classification VARCHAR (30), 
    group_company_code         VARCHAR (30), 
    column_no                  INTEGER, 
    column_position_row        INTEGER, 
    column_position_column     INTEGER 
    );