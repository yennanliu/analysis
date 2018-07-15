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
          to_currency,
          max(ts) AS ts
   FROM exchange_rates
   WHERE to_currency = 'GBP'
   GROUP BY from_currency,
            to_currency),
     lastest_exchange AS
  (SELECT e.from_currency AS from_currency,
          e.rate AS rate
   FROM exchange_rates e
   INNER JOIN lastest_exchange_ts l ON e.from_currency = l.from_currency
   AND e.to_currency = l.to_currency
   AND e.ts = l.ts),
     trans_GBP AS
  (SELECT t.user_id AS user_id,
          t.ts AS ts,
          l.from_currency AS currency,
          t.amount*l.rate AS amount_GBP
   FROM transactions t
   INNER JOIN lastest_exchange l ON l.from_currency = t.currency ),
     trans_in_GBP AS
  ( SELECT user_id,
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
ORDER BY user_id



