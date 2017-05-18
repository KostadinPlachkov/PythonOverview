import sqlite3
import sys
from datetime import datetime
import csv
from pprint import pprint
import iso8601

DB_FILENAME = "sales_catalog.db"
CATALOG_FILENAME = 'catalog.csv'
SALES_FILENAME = 'sales-10K.csv'

COLUMN_ITEM_ID = 0
COLUMN_COUNTRY = 1
COLUMN_CITY = 2
COLUMN_DATE = 3
COLUMN_PRICE = 4
COLUMN_CATEGORY = 5


KEY_ITEM_ID = 'item_id'
KEY_COUNTRY = 'country'
KEY_CITY = 'city'
KEY_DATE = 'date'
KEY_PRICE = 'price'


def main():
    with sqlite3.connect(DB_FILENAME, isolation_level = None) as connection:
        print("Connection opened")
        create_tables(connection)
        print("Tables created")
        catalog_by_item_id = load_catalog(CATALOG_FILENAME)
        import_catalog_into_db(catalog_by_item_id, connection)
        print("Catalog imported")
        sales_gen = load_sales(SALES_FILENAME)
        import_sales_into_db(sales_gen, connection)
        print("Sales imported")


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
        create table if not exists sale (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_key varchar(200) NOT NULL,
            country varchar(3),
            city_name varchar(60),
            sale_timestamp TEXT,
            price NUMERIC
        );
    """)

    cursor.execute("""
        create table if not exists catalog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_key varchar(200),
            category varchar(200)
        );
    """)


def load_catalog(filename):
    result = {}
    with open(filename, 'r', encoding = 'utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            item_id = row[COLUMN_ITEM_ID]
            category = row[COLUMN_CATEGORY]
            result[item_id] = category
    return result

def load_sales(filename: str) -> list:

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            sale = {}
            sale[KEY_ITEM_ID] = row[COLUMN_ITEM_ID]
            sale[KEY_COUNTRY] = row[COLUMN_COUNTRY]
            sale[KEY_CITY] = row[COLUMN_CITY]
            sale[KEY_DATE] = iso8601.parse_date(row[COLUMN_DATE]).isoformat()
            sale[KEY_PRICE] = float(row[COLUMN_PRICE])
            yield sale



def import_catalog_into_db(catalog_by_item_id, connection):
    cursor = connection.cursor()
    for item_id, category in catalog_by_item_id.items():
        cursor.execute(
            "insert into catalog (item_key, category) values (?, ?)",
            [item_id, category]
        )

def import_sales_into_db(sales_gen, connection):
    cursor = connection.cursor()
    for sale in sales_gen:
        cursor.execute(
            "insert into sale (item_key, country, city_name, sale_timestamp, price) values (?, ?, ?, ?, ?)",
            [sale[KEY_ITEM_ID], sale[KEY_COUNTRY], sale[KEY_CITY], sale[KEY_DATE], sale[KEY_PRICE]]
        )


if __name__ == '__main__':
    main()






