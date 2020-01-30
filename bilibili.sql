create table if not exists season(
	season_id int not null,
	aid int not null,
	title text not null,
	p_year int not null,
	p_month int not null,
	p_day int not null,
	c_year int not null,
	c_month int not null,
	c_day int not null,
	primary key ( season_id )
);