create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dummy as
with
  ancestors(ancestor, descendent) as (
    select parent, child from parents union
    select ancestor, child
      from ancestors, parents
      where parent = descendent
    )
select * from ancestors; 
