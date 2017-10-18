# customer mining sql 


####################

# vip customer 
# https://app.periscopedata.com/app/laundrapp/49843/CC---VIP-customers


SELECT first_name, last_name, email, phone FROM customers 

WHERE customers.vip = 1



####################

# Users & orders 
# https://app.periscopedata.com/app/laundrapp/179337/Yen-Playground

select 
c.id as customer_id,
c.email as email, 
c.phone,
YEAR(CURDATE())  - year(c.date_of_birth) as age, 
c.gender,
c.platform, 
c.vip,
c.fraud,
date(convert_tz(c.created_at,"utc","europe/london")) as created_date,
date(convert_tz(c.updated_at,"utc","europe/london")) as updated_date,
count(o.id) as order_count,
sum(o.original_value) as sum_original_value,
sum(o.discount_value) as sum_discount_value,
sum(o.collection_fee) as sum_collection_fee,
sum(o.delivery_fee) as sun_delivery_fee
from 
customers c 
left join 
orders o 
on c.ID = o.customer_id 
where 
date(convert_tz(c.created_at,"utc","europe/london")) >=  '2017-09-01'
and 
date(convert_tz(c.created_at,"utc","europe/london")) <=  '2017-09-30'
group by 1,2,3,4,5,6,7,8,9,10 
order by order_count desc 


####################


# Order Postcode 

select 
o.address_postcode, 
count(o.address_postcode) as postcode_count,
sum(o.original_value) as sum_original_value,
sum(o.discount_value) as sum_discount_value,
sum(o.collection_fee) as sum_collection_fee,
sum(o.delivery_fee) as sun_delivery_fee
from 
customers c 
left join 
orders o 
on c.ID = o.customer_id 
where 
date(convert_tz(c.created_at,"utc","europe/london")) >=  '2017-09-01'
and 
date(convert_tz(c.created_at,"utc","europe/london")) <=  '2017-09-30'
group by 1 
order by 2 desc 



####################

# top orders post code 


select customer_id, address_postcode, postcode_count 
from (select customer_id, address_postcode,  count(address_postcode) as postcode_count from orders 
group by customer_id, address_postcode
order by count(address_postcode)  desc
) temp where temp.address_postcode = address_postcode
group by address_postcode
order by customer_id limit 1000



####################


select 
c.id as customer_id,
date(convert_tz(o.created_at,"utc","europe/london"))  as created_at 

from customers c 
left join 
orders o 
on c.ID = o.customer_id 
where 
date(convert_tz(c.created_at,"utc","europe/london")) >=  '2017-09-01'
and 
date(convert_tz(c.created_at,"utc","europe/london")) <=  '2017-09-30'
order by 1,2 

limit 100 


####################


set @date=""
,@customer_id=0;
select
customer_id,
created_at
#LAG(created_at) OVER(ORDER BY customer_id) prev_code
,if(@customer_id!=customer_id,"",@date)temp_var2
,@customer_id :=customer_id temp_var1
,@date :=created_at temp_var3
from (
select 
c.id as customer_id,
date(convert_tz(o.created_at,"utc","europe/london"))  as created_at 
from customers c 
left join 
orders o 
on c.ID = o.customer_id 
where 
date(convert_tz(c.created_at,"utc","europe/london")) >=  '2017-09-01'
and 
date(convert_tz(c.created_at,"utc","europe/london")) <=  '2017-09-30'
order by 1,2 
limit 100  ) sub




####################


# user id and order log 

select 
c.id as customer_id,
c.email as email, 
c.phone,
YEAR(CURDATE())  - year(c.date_of_birth) as age, 
c.gender,
c.platform, 
c.vip,
c.fraud,
date(convert_tz(c.created_at,"utc","europe/london")) as created_date,
date(convert_tz(c.updated_at,"utc","europe/london")) as updated_date,
o.* 

from 
customers c 
left join 
orders o 
on c.ID = o.customer_id 
where 
date(convert_tz(c.created_at,"utc","europe/london")) >=  '2017-09-01'
and 
date(convert_tz(c.created_at,"utc","europe/london")) <=  '2017-09-30'
limit 1000








