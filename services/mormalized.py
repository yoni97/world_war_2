from db import get_db_connection


def normalize_tables():
    source_conn = get_db_connection()
    try:
        query1 = """
            CREATE TABLE target_countries (
                 target_country_id serial PRIMARY KEY,
                 target_country_name VARCHAR(100)
            create table cities(
            city_id SERIAL primary key,
            city_name varchar(255),
            country_id integer references target_countries(target_country_id),
            latitude NUMERIC(10, 6),
            longitude NUMERIC(10, 6)
            );
            create table types(
            type_id SERIAL primary key,
            type_name varchar(255)
            );
            create table industries(
            industrie_id SERIAL primary key,
            industrie_name varchar(255)
            );
            create table targets(
            target_id integer primary key,
            target_city_id integer references cities(city_id),
            target_type_id integer references types(type_id),
            target_industry_id integer references industries(industrie_id),
            target_priority integer)
            """
    cur = target_conn.cursor()
    cur.executemany(query1)
    target_conn.commit()

    s_cur = source_conn.cursor()
    s_cur.execute("SELECT * FROM customers")
