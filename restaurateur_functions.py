from constants import FOURSQUARE_LEGEND_DISCREPANCIES, YELP_LEGEND_DISCREPANCIES, GOOGLE_LEGEND_DISCREPANCIES
import psycopg2 as pg2
from psycopg2 import sql
import os


def open_local_db_admin_connection(db_name: str = 'restaurateur', username: str = 'postgres',
                                   password: str = os.getenv('pg2_pass')):
    """Establish an admin connection to restaurateur."""

    connection = pg2.connect(
        database=db_name, user=username, password=password)

    return connection


def create_source_table(cursor, data_source: str) -> None:
    """
    Creates a table using a the data provider for programmatically obtained and processed
    API data.
    """
    _table_name = data_source.lower()

    cursor.execute(
        sql.SQL('''
        CREATE TABLE IF NOT EXISTS {}
        (id SMALLSERIAL PRIMARY KEY,
        Name VARCHAR(50) NOT NULL,
        Price VARCHAR(5),
        Type TEXT,
        Rating REAL,
        RatingCount INT,
        Source VARCHAR(20));
        ''').format(sql.Identifier(_table_name)))

    print(f'Created table {_table_name} successfully!')


def create_source_tables(cursor, data_sources: tuple = (FOURSQUARE_LEGEND_DISCREPANCIES['Source'],
                                                        YELP_LEGEND_DISCREPANCIES['Source'],
                                                        GOOGLE_LEGEND_DISCREPANCIES['Source'])) -> None:
    """
    Creates a table for each data provider included in the tuple.
    """
    for source in data_sources:
        create_source_table(cursor, source)
