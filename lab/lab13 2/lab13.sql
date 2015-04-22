.read data.sql

-- Q1
CREATE TABLE flight_costs as
  -- REPLACE THIS LINE
  with helper(day, previous_price, price) as (
    select 1, 0, 20 union
    select 2,0, 30 union
    select 3, 30, 40 union
    select day + 1, price, (price + previous_price)/2 + 5 * ((day + 1) % 7) from helper
    where day + 1 <= 25  and day >= 3
  )
  SELECT day, price from helper;

-- Q2
CREATE TABLE schedule as
with helper(start, end, list, num, total) as (
    select departure, arrival, departure || ", " || arrival, 1, price from flights where
    departure="SFO" union
    select start, arrival, list || ", " || arrival, num + 1, total + price from helper, flights
    where end = departure and num + 1 <= 2
)
SELECT list,total from helper where end ="PDX" order by total ASC;


-- Q3
CREATE TABLE shopping_cart as
  -- REPLACE THIS LINE
  SELECT 'YOUR CODE HERE';


-- Q4
CREATE TABLE number_of_options as
  -- REPLACE THIS LINE
  select count(distinct meat) from  main_course;


-- Q5
CREATE TABLE calories as
  -- REPLACE THIS LINE
  select count(*) from main_course as m, pies as p where m.calories + p.calories < 2500;


-- Q6
CREATE TABLE healthiest_meats as
  -- REPLACE THIS LINE
  SELECT 'YOUR CODE HERE';


-- Q7
CREATE TABLE average_prices as
  -- REPLACE THIS LINE
  SELECT 'YOUR CODE HERE';


-- Q8
CREATE TABLE lowest_prices as
  -- REPLACE THIS LINE
  SELECT 'YOUR CODE HERE';


-- Q9
CREATE TABLE shopping_list as
  -- REPLACE THIS LINE
  SELECT 'YOUR CODE HERE';


-- Q10
CREATE TABLE total_bandwidth as
  -- REPLACE THIS LINE
  SELECT 'YOUR CODE HERE';

