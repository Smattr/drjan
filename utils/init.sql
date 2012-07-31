create table users (
    id integer,
    uid integer,
    gid integer,
    user text,
    name text,
    service text
);

create table groups (
    id integer,
    gid integer,
    group text,
    service text
);

create table membership (
    id integer,
    user_fk integer,
    group_fk integer
);
