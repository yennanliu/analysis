CREATE TABLE target_vm_9000_vm_transaction_201901 AS
SELECT t.*
FROM spectrum.transaction_201903 t
WHERE (t.branch_number,
       t.customer_number,
       t.equipment_code,
       t.column_no) IN
    (SELECT branch_number,
            customer_number,
            equipment_code,
            column_no
     FROM spectrum.target_vm)