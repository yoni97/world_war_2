from psycopg2 import extensions

from db import get_db_connection, connection_pool


def normalize_tables():
    source_conn = get_db_connection()
    try:
        query1 = """
            CREATE TABLE IF NOT EXISTS target_countries (
                 target_country_id SERIAL PRIMARY KEY,
                 target_country_name VARCHAR(100)
                 )
                 """

        query2 = """
            create table IF NOT EXISTS cities(
            city_id SERIAL primary key,
            city_name varchar(255),
            country_id integer references target_countries(target_country_id),
            latitude NUMERIC(10, 6),
            longitude NUMERIC(10, 6)
            );
            """

        query3 = """
            create table IF NOT EXISTS types(
            type_id SERIAL primary key,
            type_name varchar(255)
            );
            """

        query4 = """
            create table IF NOT EXISTS industries(
            industrie_id SERIAL primary key,
            industrie_name varchar(255)
            );
            """

        query5 = """
            create table IF NOT EXISTS targets(
            target_id SERIAL primary key,
            target_city_id integer references cities(city_id),
            target_type_id integer references types(type_id),
            target_industry_id integer references industries(industrie_id),
            target_priority varchar(255)
            );
            """
        source_conn.commit()

        cur: extensions.cursor = source_conn.cursor()
        all_queries = [query1, query2, query3, query4, query5]
        for query in all_queries:
            cur.execute(query)
            source_conn.commit()

        s_cur = source_conn.cursor()
        s_cur.execute("SELECT * FROM mission")

        while True:
            mission_row = s_cur.fetchone()
            if mission_row is None:
                break
            country_name = mission_row[14]
            city_name = mission_row[15]
            target_latitude = mission_row[19]
            target_longitude = mission_row[20]
            target_type = mission_row[16]
            target_industry = mission_row[17]
            target_priority = mission_row[18]

            cur.execute(f"INSERT INTO target_countries (target_country_name) VALUES (%s) RETURNING target_country_id;",
                        (country_name,))
            country_id = cur.fetchone()[0]

            cur.execute("INSERT INTO cities (city_name,country_id, latitude, longitude) VALUES(%s,%s,%s,%s) RETURNING city_id;",
                        (city_name, country_id, target_latitude, target_longitude))
            target_city_id = cur.fetchone()[0]

            cur.execute("INSERT INTO types (type_name) VALUES (%s) RETURNING type_id;" ,(target_type,))
            type_id = cur.fetchone()[0]

            cur.execute(
                "INSERT INTO industries (industrie_name) VALUES (%s) RETURNING industrie_id;",
                (target_industry,))
            target_industrie_id = cur.fetchone()[0]

            cur.execute(
                "INSERT INTO targets (target_city_id, target_type_id, target_industry_id, target_priority) VALUES (%s, %s, %s, %s) RETURNING target_id;",
                (target_city_id, type_id, target_industrie_id, target_priority))
            source_conn.commit()

    except Exception as e:
        print(e)

    finally:
        connection_pool.closeall()

print(normalize_tables())

