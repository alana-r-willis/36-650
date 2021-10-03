alter table player_bios
	add column inches numeric;
	
update player_bios
	set inches = 12*split_part(height,'-',1)::integer + split_part(height,'-',2)::integer;
	
alter table player_bios
	drop column height;
	
alter table player_bios
	rename inches to height;
