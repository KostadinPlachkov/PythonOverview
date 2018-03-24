import sqlite3
import csv
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
    city = input("Enter city:")
    with sqlite3.connect(DB_FILENAME, isolation_level=None) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            select item_key, sale_timestamp, price
            from sale
            where
            city_name = (?)
            order by sale_timestamp;
            """,
            [city]
        )
        data = cursor.fetchall()
        if data:
            print("Sales in %s:" % city)
            for row_number, row in enumerate(data, start = 1):
                item, date, price = row
                print(row_number, "Product #: {}   date/hour: {}   price: {:.2f}".format(item, date, price))
        else:
            print("No data for sales in", city)



if __name__ == '__main__':
    main()
