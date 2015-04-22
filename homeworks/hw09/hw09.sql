create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
select d.name , s.size from dogs as d, sizes as s WHERE d.height > s.min AND d.height <= s.max;


-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
select p.child from parents as p, dogs as d WHERE p.parent = d.name ORDER BY d.height DESC;


-- Sentences about siblings that are the same size
create table sentences as
with sizes(name, sizes, parent) as (
  select "abraham", "toy", "fillmore" union
  select "barack", "standard", "abraham"  union
  select "clinton", "standard", "abraham" union
  select "delano", "standard", "fillmore" union
  select "eisenhower", "mini", "None" union
  select "filmore" , "mini", "eisenhower" union
  select "grover", "toy", "fillmore" union
  select "herbert", "mini", "delano" 
)
select a.name || " and " || b.name || " are " || b.sizes || " siblings" from sizes as a, sizes as b WHERE a.sizes = b.sizes AND a.name < b.name AND a.parent = b.parent;


-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
with stacks(name, last_dog_height, n, total_height) as (
  select name, height, 1, height from dogs union
  select previous.name || ", " || next.name, next.height, n + 1, previous.total_height + next.height 
    from stacks as previous, dogs as next 
    where n < 4 and last_dog_height < next.height
) 
select name, total_height from stacks where n=4 and total_height > 170 order by total_height ASC; 



create table tallest as
select max(height), name from dogs GROUP BY (height/10) having count(*) > 1;


-- All non-parent relations ordered by height difference
create table non_parents as
select "REPLACE THIS LINE WITH YOUR SOLUTION";


