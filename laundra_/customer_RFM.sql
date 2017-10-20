SET @var = 0 ,
    @var1 = 0 ,
    @var2 = 0 ;


SELECT id,
       Name,
       email -- ,address_line_1
-- ,address_line_2
-- ,address_town
-- ,postcode
,
       Frequency,
       Monetory,
       Recency,
       recency_grouping
FROM
  ( SELECT id ,
           Recency ,
           floor( (100 * counter2 / total_customers) / 20 ) + 1 recency_grouping ,
           Frequency ,
           freq_grouping ,
           Monetory ,
           monetory_grouping ,
           concat(floor((100 * counter2 / total_customers) / 20) + 1 , freq_grouping , monetory_grouping , email ) rfm ,
           Name,
           address_line_1,
           address_line_2,
           address_town,
           postcode,
           opt_in,
           email from
     (SELECT *, @var2 := @var2 + 1 counter2
      FROM
        ( SELECT id , Recency , Frequency , Monetory , freq_grouping , floor( (100 * counter1 / total_customers) / 20 ) + 1 monetory_grouping , total_customers ,Name,address_line_1,address_line_2,address_town,postcode,opt_in,email
         FROM
           ( SELECT * , @var1 := @var1 + 1 counter1
            FROM
              ( SELECT id , Recency , Frequency , Monetory , floor( (100 * counter / total_customers) / 20 ) + 1 freq_grouping , total_customers ,Name,address_line_1,address_line_2,address_town,postcode,opt_in,email
               FROM
                 ( SELECT * , @var := @var + 1 counter
                  FROM
                    ( SELECT c.id , convert_tz(max(orders.created_at), "utc", "europe/london") Recency , count(orders.id) Frequency , sum(orders.total_value) Monetory ,concat(c.first_name, " ", c.last_name) Name , orders.address_line_1 address_line_1,orders.address_line_2 address_line_2, orders.address_town address_town , orders.address_postcode postcode ,c.opt_in ,c.email
                     FROM orders
                     JOIN customers c ON c.id = orders.customer_id
                     WHERE c.id NOT IN ( 32997 , 49629 , 46618 )
                       AND [order_filter] #and c.opt_in=1
                     GROUP BY 1
                     ORDER BY Frequency ASC ) rfm join
                    ( SELECT count(DISTINCT customer_id) + 1 total_customers
                     FROM orders
                     WHERE [order_filter] ) pc ) fgroup
               GROUP BY 1
               ORDER BY fgroup.Monetory ASC ) mordered ) mgroup
         GROUP BY 1
         ORDER BY recency ASC )rordered ) rgrouping ) rfm_filter
WHERE rfm IN (555 )
  AND Recency>=curdate() - interval 30 DAY #and opt_in=1 -- order by Monetory desc,  Frequency desc
-- limit 200 ,150