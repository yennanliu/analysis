create table filtered_9000_vm_transaction_201901 as 
SELECT 
*
FROM spectrum.transaction_201901 t
WHERE t.equipment_code IN
    (SELECT vm_id
     FROM public.vm_9000_list);