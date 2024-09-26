from flask_sqlalchemy import SQLAlchemy
import psycopg2
from psycopg2 import pool

connection_pool = psycopg2.pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            dbname="wwi_missions",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )

def get_db_connection():
    if connection_pool:
        conn = connection_pool.getconn()
        return conn

def release_db_connection(conn):
    connection_pool.putconn(conn)

db = SQLAlchemy()