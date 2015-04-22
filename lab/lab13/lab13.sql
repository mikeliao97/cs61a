.read data.sql

-- Q1
CREATE TABLE flight_costs as
  with costs(day, previous, current) as (
    select 1, 0, 20 union
    select 2, 20, 30 union
    select 3, 30, 40 union
    select day + 1, current, (previous + current)/2 + 5*((day + 1) % 7) from costs where day <= 24 and day >= 3
  ) 
SELECT day, current from costs;



--Find the cheapest set of flights from SFO to PDX but do not include
--options with more than two flights! You should generate at able 
--with the following columns
--The set of airports that the flights pass through
--Be sure to order your table from the cheapest to most expensive option

-- Stuff is in the flights table
-- num_flights can't be more than 3
CREATE TABLE schedule as
with local_flights(num, list, previous, cost) as (
  select 1, departure || ", " || arrival, arrival, price from flights where departure="SFO" union
  select num + 1, l.list || ", " || f.arrival, f.arrival, l.cost + f.price from flights as f, local_flights as l WHERE f.departure = l.previous and l.num <= 1 
)
SELECT list, cost from local_flights where previous="PDX" order by cost; 

-- Q3
-- you order needs to be defined:
-- 1. Order by budgets least first
-- 2. Order by Alphabetically
-- 3. Use a with table that creates a list that subtracts stuff
CREATE TABLE shopping_cart as
with local_cart(budget, list, previous) as (
  select 60 - price, item, price from supermarket where 60 - price >= 0 union 
  select local.budget - next.price, local.list || ", " || next.item, next.price from supermarket as next, local_cart as local 
  where budget - next.price >= 0 and next.price >= previous 
)
select list, budget from local_cart order by budget, list;
--SELECT list, budget from local_cart order by budget ASC, list;


-- Q4
CREATE TABLE number_of_options as

SELECT count(distinct meat) from main_course;


-- Q5
CREATE TABLE calories as
with local_calories(calories) as (
  select a.calories + b.calories from main_course as a, pies as b where a.calories + b.calories < 2500
)
SELECT count(*) from local_calories;



-- Q6
-- For this problem you want to pair tables main_course to  pies. 
-- definitely have to group by meats. 
CREATE TABLE healthiest_meats as
SELECT meat, min(a.calories + b.calories) as calories from main_course as a,
pies as b group by meat having max(a.calories + b.calories) < 3000;


-- Q7
CREATE TABLE average_prices as
SELECT category, avg(msrp) from products group by category;


-- Q8
CREATE TABLE lowest_prices as
select item, store, min(price) from inventory group by item;


-- Q9
CREATE TABLE shopping_list as
with local_list(name, rating) as (
  select name, min(MSRP/rating) from products group by category
)
select name, store from local_list, lowest_prices where item=name;

-- Q10
CREATE TABLE total_bandwidth as
select sum(s.MiBs) from stores as, shopping_list as sl where s.store = sl.store;

