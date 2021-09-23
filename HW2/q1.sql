create table rdata (
postgres(# id serial primary key, a varchar(5), b varchar(5), 
moment date, x numeric (5,2));

postgres=# select * from rdata;
 id | a | b | moment | x 
----+---+---+--------+---
(0 rows)
