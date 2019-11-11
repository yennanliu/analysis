CREATE
        OR REPLACE VIEW filtered_10_vm_transaction AS WITH t_2014 AS
  (SELECT *
   FROM "suntory"."transaction"
   WHERE dt >= '201401'
     AND dt <= '201412'
     AND equipment_code IN ('42060652',
                            '41062022',
                            '1635412',
                            '42009165',
                            '41006781',
                            '42108489',
                            '42097432',
                            '1634993',
                            '1711952',
                            '42011428') ),
                        t_2015 AS
  (SELECT *
   FROM "suntory"."transaction"
   WHERE dt >= '201501'
     AND dt <= '201512'
     AND equipment_code IN ('42060652',
                            '41062022',
                            '1635412',
                            '42009165',
                            '41006781',
                            '42108489',
                            '42097432',
                            '1634993',
                            '1711952',
                            '42011428') ),
                        t_2016 AS
  (SELECT *
   FROM "suntory"."transaction"
   WHERE dt >= '201601'
     AND dt <= '201612'
     AND equipment_code IN ('42060652',
                            '41062022',
                            '1635412',
                            '42009165',
                            '41006781',
                            '42108489',
                            '42097432',
                            '1634993',
                            '1711952',
                            '42011428') ),
                        t_2017 AS
  (SELECT *
   FROM "suntory"."transaction"
   WHERE dt >= '201701'
     AND dt <= '201712'
     AND equipment_code IN ('42060652',
                            '41062022',
                            '1635412',
                            '42009165',
                            '41006781',
                            '42108489',
                            '42097432',
                            '1634993',
                            '1711952',
                            '42011428') ),
                        t_2018 AS
  (SELECT *
   FROM "suntory"."transaction"
   WHERE dt >= '201801'
     AND dt <= '201812'
     AND equipment_code IN ('42060652',
                            '41062022',
                            '1635412',
                            '42009165',
                            '41006781',
                            '42108489',
                            '42097432',
                            '1634993',
                            '1711952',
                            '42011428') ),
                        t_2019 AS
  (SELECT *
   FROM "suntory"."transaction"
   WHERE dt >= '201901'
     AND dt <= '201906'
     AND equipment_code IN ('42060652',
                            '41062022',
                            '1635412',
                            '42009165',
                            '41006781',
                            '42108489',
                            '42097432',
                            '1634993',
                            '1711952',
                            '42011428') )
SELECT *
FROM t_2014
UNION
SELECT *
FROM t_2015
UNION
SELECT *
FROM t_2016
UNION
SELECT *
FROM t_2017
UNION
SELECT *
FROM t_2018
UNION
SELECT *
FROM t_2019;