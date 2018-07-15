
/*
redo the same query ( as GBP_spend_user.sql ),
but use the latest exchange rate smaller 
or equal then the transaction timestamp. 
should have the two columns: 
user_id, total_spent_gbp, ordered by user_id
*/ 


/*
get all exchange rate history with ts (currency -> GBP) 
then inner join transaction table with above CTE 
on same from_currency and timestamp of  exchange rate < = timestamp of transaction
*/

/*


WITH exchange_ts AS
  (SELECT ts,
        from_currency,
        to_currency,
        rate 
   FROM exchange_rates
   WHERE to_currency = 'GBP'),
        trans_GBP AS
  (SELECT t.user_id AS user_id,
          t.ts AS ts,
          t.currency AS currency,
          t.amount*e.rate AS amount_GBP
   FROM transactions t
   INNER JOIN exchange_ts e
   on e.from_currency = t.currency
   where e.ts <= t.ts )
SELECT *
FROM trans_exchange
ORDER BY user_id,
         ts


*/ 



WITH exchange_ts AS
  (SELECT ts,
  		  from_currency,
  		  to_currency,
  		  rate 
   FROM exchange_rates
   WHERE to_currency = 'GBP'),
  exchange_ts_  as 
 ( select 
*, 
-- if ts_lag = null, replace with  '2018-03-01T00:00:00Z'
lag(ts,1 , '2018-03-01T00:00:00Z') over  (partition by from_currency, to_currency  order by ts) as ts_lag
from exchange_rates WHERE to_currency = 'GBP' ), 
        trans_GBP AS
  (SELECT t.user_id AS user_id,
          t.ts AS ts,
          t.currency AS currency,
          t.amount*e.rate AS amount_GBP,
          t.amount as amount
   FROM transactions t
   INNER JOIN exchange_ts_ e
   on e.from_currency = t.currency
   and (  t.ts  <=  e.ts  
   and e.ts_lag <= t.ts   )
   or 
   (e.ts_lag <= t.ts ) 
   )
SELECT *
FROM trans_GBP
ORDER BY user_id,
         ts




