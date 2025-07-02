import os
import pymysql

# Mude o user e senha do BD aqui 

DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "root"
DB_NAME = "db_maracujina"
DB_PORT = 3306


def dbConnect(database: str | None = None):

    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT,
        database=database or DB_NAME,
        connect_timeout=5,
    )
