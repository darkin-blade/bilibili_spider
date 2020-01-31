create table if not exists season(
	season_id int not null,
	aid int not null,
	id int not null,
	title text not null,
	p_year int not null,
	p_month int not null,
	p_day int not null,
	c_year int not null,
	c_month int not null,
	c_day int not null,
	primary key ( season_id )
);

insert into season (season_id, aid, title, p_year, p_month, p_day, c_year, c_month, c_day)
	values
	(0, 0, '双方的发生地方''sadfsadfasd', 0, 0, 0, 0, 0, 0);

create table if not exists failed(
	season_id int not null,
	aid int not null,
	id int not null,
	primary key ( season_id )
);

insert into failed (season_id, aid)
	values
	(3097, ),
	(3128, ),
	(1308, ),
	(3407, ),
	(2894, ),
	(9166, );