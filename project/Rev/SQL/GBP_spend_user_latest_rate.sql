
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

WITH exchange_ts AS
  (SELECT ts,
          from_currency,
          to_currency,
          rate
   FROM exchange_rates
   WHERE to_currency = 'GBP'),
     exchange_ts_ AS
  (SELECT *,
          lag(ts, -1, '2019-01-01T00:00:00Z') OVER (PARTITION BY from_currency,
                                                                 to_currency
                                                    ORDER BY ts) AS ts_lag
   FROM exchange_rates
   WHERE to_currency = 'GBP' ),
     trans_GBP AS
  (SELECT t.user_id AS user_id,
          t.ts AS ts,
          t.currency AS currency,
          t.amount*e.rate AS amount_GBP
   FROM transactions t
   INNER JOIN exchange_ts_ e ON e.from_currency = t.currency
   AND (t.ts >= e.ts
        AND e.ts_lag > t.ts) ),
     trans_in_GBP AS
  (SELECT user_id,
          ts,
          currency,
          amount AS amount_gbp
   FROM transactions
   WHERE currency = 'GBP' )
SELECT *
FROM trans_GBP
UNION ALL
SELECT *
FROM trans_in_GBP
ORDER BY user_id,
         ts




