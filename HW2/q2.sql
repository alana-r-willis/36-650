drop table rdata;
DROP TABLE

create table rdata (
postgres(# id serial primary key,
postgres(# a varchar(5) unique not null,
postgres(# b varchar(5) unique not null,
postgres(# moment date not null default '2020-01-01',
postgres(# x numeric(5,2) check (x>0)
postgres(# );
