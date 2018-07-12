/*
query that breakdown of spend in GBP by each user.
Use the exchange rate with largest timestamp
*/ 

/*
get the lastest exchange rate for each currency to GBP 
map transaction amount on CTE above to transform 
all transaction in GBP with lastest exchange rate 
*/ 


WITH lastest_exchange_ts AS
  (SELECT from_currency,
          max(ts)
   FROM exchange_rates
   WHERE to_currency = 'GBP'
   GROUP BY from_currency),
        lastest_exchange AS
  (SELECT e.from_currency,
          e.rate
   FROM exchange_rateser e
   INNER JOIN lastest_exchange_ts l ON e.from_currency = l.from_currency),
        trans_GBP AS
  (SELECT t.user_id AS user_id,
          t.ts AS ts,
          l.to_currency AS currency,
          t.amount*l.rate AS amount_GBP,
   FROM transactions t
   INNER JOIN lastest_exchange l)
SELECT *
FROM trans_exchange
ORDER BY user_id,
         ts




