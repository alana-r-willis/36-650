create table new_table (
	player integer references more_player_stats,
	prl numeric,
	position text);

insert into new_table (player,prl) (select id, round(per - 67*va/(gp*minutes),1) from more_player_stats);

update new_table
	set position = 'PF'
	where prl >= 11.3;

update new_table
	set position = 'PG'
	where prl >= 10.8 AND prl < 11.3;

update new_table
	set position = 'C'
	where prl >= 10.6 AND prl < 10.8;
	
update new_table
	set position = 'SG/SF'
	where prl >= 0 AND prl < 10.6;


