create table articles(
    id char(14) not null primary key,
    title char(64),
    author char(64),
    tag_id tinyint,
    flag_id tinyint,
    create_datetime datetime,
    context_html text,
    ps_html text
)default charset=utf8