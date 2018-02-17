


sql = {

'sql_test' : """

SELECT * FROM rw.blue_move
limit 10 

""",

# --------------------		

'sql_trips':"""

  WITH customer_id AS
(SELECT member_id
FROM ana.members
WHERE ROLE = 'customer' )
SELECT t.booking_start_date,
   t.trip_start_date,
   date(t.booking_start_date) AS book_start_day,
   date(t.trip_start_date) AS trip_start_day,
   t.vin,
   t.member_id,
   sz.name AS start_zone_name,
   ez.name AS end_zone_name,
   t.start_lat,
   t.start_lon,
   t.end_lat,
   t.end_lon,
   t.distance,
   t.trip_duration
FROM prc.trips t
LEFT JOIN rw.quartiers sz ON st_contains(sz.geom, t.start_pos_gis)
LEFT JOIN rw.quartiers ez ON st_contains(ez.geom, t.end_pos_gis)
WHERE member_id  IN
(SELECT *
 FROM customer_id)
AND trip_duration > 0
AND date(t.trip_start_date) >= '2018-01-01'

""",

# --------------------     


'sql_trips_agg':"""

WITH customer_id AS
  (SELECT member_id
   FROM ana.members
   WHERE ROLE = 'customer' )
SELECT date(t.trip_start_date) AS trip_start_day,
       extract(hour
               FROM t.trip_start_date) AS trip_start_hour,
       ROUND((start_lat)::numeric,3) AS start_lat,
       ROUND((start_lon)::numeric,3) AS start_lon,
       count(*) AS pickups
FROM prc.trips t
WHERE member_id  IN
    (SELECT *
     FROM customer_id)
  AND trip_duration > 0
  AND date(t.trip_start_date) >= '2016-09-01'
GROUP BY 1,
         2,
         3,
         4
ORDER BY 1,
         2,
         3,
         4
         
"""}


sql_agg = {
  
'day_zone_trip' : """


WITH customer_id AS
  (SELECT member_id
   FROM ana.members
   WHERE ROLE = 'customer' )
SELECT date(t.trip_start_date) AS trip_start_day,
       sz.name AS start_zone_name,
       sz.zone_id AS start_zone_id,
       count(*) AS pickups
FROM prc.trips t
LEFT JOIN rw.quartiers sz ON st_contains(sz.geom, t.start_pos_gis)
WHERE member_id IN
    (SELECT *
     FROM customer_id)
  AND trip_duration > 0
  AND date(t.trip_start_date) >= '2017-01-01'
  AND sz.name IS NOT NULL
GROUP BY 1,
         2,
         3


"""

# --------------------    



}



# --------------------    


sql_itime = {
  
'itime_ '= """


SELECT 
       lag(round((idle_time/(60*60*24))::numeric,2)) OVER (PARTITION BY vehicle_id
                                                           ORDER BY timestamp_live_vec_table DESC) AS lag_idle_day,
                                                          *
FROM
  (SELECT DISTINCT round((idle_time/(60*60*24))::numeric,2) AS idle_days,
                   round((idle_time/(60*60))::numeric,2) AS idle_hours,
                   vehicle_id,
                   idle_time,
                   timestamp_live_vec_table,
                   date(timestamp_live_vec_table) as date,
                   lat,
                   lon
   FROM i_time_table
   WHERE date(i_time_table.timestamp_live_vec_table) >= '2018-01-01' ) sub
ORDER BY vehicle_id,
         timestamp_live_vec_table



"""



}







