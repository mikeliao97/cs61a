create table pizzas as
  select "Pizzahhh" as name, 12 as open, 15 as close union
  select "La Val's"        , 11        , 22          union
  select "Sliver"          , 11        , 20          union
  select "Cheeseboard"     , 16        , 23          union
  select "Emilia's"        , 13        , 18;

create table meals as
  select "breakfast" as meal, 11 as time union
  select "lunch"            , 13         union
  select "dinner"           , 19         union
  select "snack"            , 22;

--Strategy for number 1
-- make sure meal2 > meal1 - 6. make sure both meals are within the time of pizza
-- Two meals at the same place
create table double as
select meal1.meal, meal2.meal, name FROM meals as meal1, meals as meal2, pizzas 
        WHERE meal2.time - meal1.time > 6;

-- Strategy for number 2
-- It's in alphabetical order 
-- so for meals table, it's 4 rows so theres only 4 rows
-- |breakfast| 3| Cheese
-- so why do you need to use the max option in the with statement?
--
-- Pizza options for every meal
create table options as
with options(meal, list, last_place,num_meals, pizza_time) as (
  select meal, min(name), name, 1, time from meals, pizzas where time >= open and time <= close group by meal union 
  select meal, previous.list || ", " ||  next.name, next.name, num_meals + 1, pizza_time 
    from options as previous, pizzas as next where last_place < next.name 
    and pizza_time <= next.close and pizza_time >= next.open 
)
select meal, max(num_meals), list from options group by meal order by pizza_time; 


