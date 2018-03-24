from datetime import datetime, timedelta
import iso8601
import os
import sys
from pprint import pprint
import csv
import operator

COLUMN_PRICE = 4
COLUMN_DATETIME = 3
COLUMN_ID = 0
COLUMN_CITY = 2
COLUMN_CATEGORIES = -3


def calc_starting_ending_time(file_sales):
    dt_obj_list = []
    with open(file_sales, encoding = "utf-8") as fs:
        reader = csv.reader(fs)
        for row in reader:
            dt_obj_list.append(iso8601.parse_date(row[COLUMN_DATETIME]))
    starting_date = min(dt_obj_list)
    ending_date = max(dt_obj_list)
    return starting_date, ending_date


def calc_summary(file_sales):
    price_list = []
    with open(file_sales, encoding = "utf-8") as fs:
        reader = csv.reader(fs)
        for row in reader:
            price = float(row[COLUMN_PRICE])
            price_list.append(price)
    sales_count = len(price_list)
    sales_sum = sum(price_list)
    average_price = sales_sum / sales_count
    starting_date, ending_date = calc_starting_ending_time(file_sales)
    print("\n")
    print("Summary")
    print("-------")
    print("Sales made: {count}".format(count = sales_count))
    print("Income from sales: {:.2f}".format(sales_sum))
    print("Average price of a payment: {:.2f}".format(average_price))
    print("Starting point of the data: {}".format(starting_date))
    print("Ending point of the data: {}".format(ending_date))


def calc_top_cities(file_sales, top = 5):
    cities_prices_dict = {}
    with open(file_sales, encoding = "utf-8") as fs:
        reader = csv.reader(fs)
        for row in reader:
            price = float(row[COLUMN_PRICE])
            city = row[COLUMN_CITY]
            if city in cities_prices_dict:
                cities_prices_dict[city] += price
            else:
                cities_prices_dict[city] = price
    cities_prices_dict = sorted(cities_prices_dict.items(), key = operator.itemgetter(1))[::-1]
    print("Top %d cities by sales" % top)
    print("---------------------")
    for city, price in cities_prices_dict[:top]:
        print(city, ": %.2f" % price)


def calc_top_date_hours(file_sales, top = 5):
    dt_prices_dict = {}
    with open(file_sales, encoding = "utf-8") as fs:
        reader = csv.reader(fs)
        for row in reader:
            price = float(row[COLUMN_PRICE])
            dt = row[COLUMN_DATETIME]
            dt_obj = iso8601.parse_date(dt)
            dt_obj = dt_obj.replace(minute = 0, second = 0)
            if dt_obj in dt_prices_dict:
                dt_prices_dict[dt_obj] += price
            else:
                dt_prices_dict[dt_obj] = price
    dt_prices_dict = sorted(dt_prices_dict.items(), key = operator.itemgetter(1))[::-1]
    print("Top %d sales by date" % top)
    print("-------------------")
    for date, price in dt_prices_dict[:top]:
        print(date, ": %.2f" % price)


def calc_top_products(file_sales, file_catalog, top = 5):
    category_id_dict = {}
    id_price_dict = {}
    category_price_dict = {}
    with open(file_sales, encoding = "utf-8") as fs:
        with open(file_catalog, encoding = "utf-8") as fc:
            reader_fs = csv.reader(fs)
            reader_fc = csv.reader(fc)
            for row in reader_fc:
                category = row[COLUMN_CATEGORIES]
                id_obj = row[COLUMN_ID]
                if category in category_id_dict:
                    category_id_dict[category] += [id_obj]
                else:
                    category_id_dict[category] = [id_obj]
            for row in reader_fs:
                price = float(row[COLUMN_PRICE])
                id_obj = row[COLUMN_ID]
                id_price_dict[id_obj] = price
            for category, id_objs in category_id_dict.items():
                for id_obj, price in id_price_dict.items():
                    if id_obj in id_objs:
                        if category in category_price_dict:
                            category_price_dict[category] += price
                        else:
                            category_price_dict[category] = price
                    else:
                        continue
            category_price_dict = sorted(category_price_dict.items(), key = operator.itemgetter(1))[::-1]
            print("Top %d sales by categories" % top)
            print("-------------------------")
            for category, price in category_price_dict[:top]:
                print(category, ": %.2f" % price)

if __name__ == '__main__':
    if len(sys.argv) >= 3:
        file_catalog = sys.argv[1]
        file_sales = sys.argv[2]
        calc_summary(file_sales)
        print("\n")
        calc_top_products(file_sales, file_catalog)
        print("\n")
        calc_top_cities(file_sales)
        print("\n")
        calc_top_date_hours(file_sales)
    else:
        print("Please provide a catalog file as a first parameter and file with sales as second")