import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # Required to load the previously defined environment variables


def init_conn():
    connection = psycopg2.connect(host=os.environ.get('PG_HOST'),
                                  port=os.environ.get('PG_PORT'),
                                  user=os.environ.get('PG_USER'),
                                  password=os.environ.get('PG_PASSWORD')
                                  )

    connection.autocommit = True  # Ensure data is added to the database immediately after write commands
    cursor = connection.cursor()
    cursor.execute('SELECT %s as connected;', ('Connection to postgres successful!',))
    print(cursor.fetchone())

    return connection


def init_db_conn(db_name):
    print(db_name)
    connection = psycopg2.connect(dbname=db_name,
                                  host=os.environ.get('PG_HOST'),
                                  port=os.environ.get('PG_PORT'),
                                  user=os.environ.get('PG_USER'),
                                  password=os.environ.get('PG_PASSWORD')
                                  )

    connection.autocommit = True  # Ensure data is added to the database immediately after write commands
    cursor = connection.cursor()
    cursor.execute('SELECT %s as connected;', ('Connection to postgres successful!',))
    print(cursor.fetchone())

    return connection
