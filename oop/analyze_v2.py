from pprint import pprint

import csv
import iso8601
import time

CATALOG_FILENAME = 'catalog.csv'
SALES_FILENAME = 'sales-1M.csv'

COLUMN_ITEM_ID = 0
COLUMN_COUNTRY = 1
COLUMN_CITY = 2
COLUMN_TS = 3
COLUMN_PRICE = 4
COLUMN_CATEGORY = 5

KEY_ITEM_ID = 'item_id'
KEY_COUNTRY = 'country'
KEY_CITY = 'city'
KEY_TS = 'ts'
KEY_PRICE = 'price'


def main():
    catalog = load_catalog(CATALOG_FILENAME)
    print("Analysis...")
    print("Please wait")

    analyzers = [
        TotalsAnalyzer(),
        AmountsByCategoryAnalyzer(catalog),
        AmountsByCityAnalyzer(catalog),
        AmountsByHourAnalyzer(catalog),
    ]

    load_sales_generator_object = load_sales(SALES_FILENAME)
    for sale in load_sales_generator_object:
        for a in analyzers:
            a.analyze_sale(sale)

    for a in analyzers:
        a.print_results()


# -----------------------------------------------


class BaseAnalyzer:
    def analyze_sale(self, sale):
        pass

    def print_results(self):
        pass


class TotalsAnalyzer(BaseAnalyzer):
    def __init__(self):
        super().__init__()
        self.total_count = 0
        self.total_amount = 0
        self.min_timestamp = None
        self.max_timestamp = None

    def analyze_sale(self, sale):
        self.total_amount += sale[KEY_PRICE]
        self.total_count += 1

        ts = sale[KEY_TS]
        if self.min_timestamp is None or ts < self.min_timestamp:
            self.min_timestamp = ts
        if self.max_timestamp is None or ts > self.max_timestamp:
            self.max_timestamp = ts

    def print_results(self):
        print("""
Summary
---------
    Total sales: {total_count}
    Total price: {total_amount:.2f} €
    Average price for a product: {average_price:.2f} €
    Staring date: {min_ts}
    Ending date: {max_ts}
    """.format(
            total_count=self.total_count,
            total_amount=self.total_amount,
            average_price=self.total_amount / self.total_count if self.total_count else None,
            min_ts=self.min_timestamp,
            max_ts=self.max_timestamp,
        ))


class AmountsGroupedAnalyzer(BaseAnalyzer):
    group_by_title = ''

    def __init__(self, catalog):
        super().__init__()
        self.amounts_grouped = {}  # key : category name  ,  value : accumulated sum of sales
        self.catalog = catalog

    def analyze_sale(self, sale):
        price = sale[KEY_PRICE]
        group_by_value = self.get_group_by_value(sale)
        if group_by_value not in self.amounts_grouped:
            self.amounts_grouped[group_by_value] = 0
        self.amounts_grouped[group_by_value] += price

    def get_group_by_value(self, sale):
        pass

    def print_results(self):
        # [ (category1, sales_amount1), (category2, sales_amount2),...]
        amounts_grouped_sorted = list(self.amounts_grouped.items())
        amounts_grouped_sorted.sort(key=lambda kv: kv[1], reverse=True)

        print("""
Sales by {} (top 5)
-----------------------------
    """.format(self.group_by_title))
        for category_name, total_amount in amounts_grouped_sorted[:5]:
            print("     {}: {:.2f} €".format(category_name, total_amount))


class AmountsByCategoryAnalyzer(AmountsGroupedAnalyzer):
    group_by_title = 'categories'

    def get_group_by_value(self, sale):
        item_id = sale[KEY_ITEM_ID]
        return self.catalog.get(item_id, None)


class AmountsByCityAnalyzer(AmountsGroupedAnalyzer):
    group_by_title = 'cities'

    def get_group_by_value(self, sale):
        return sale[KEY_CITY]


class AmountsByHourAnalyzer(AmountsGroupedAnalyzer):
    group_by_title = 'hours'

    def get_group_by_value(self, sale):
        ts = sale[KEY_TS]
        ts = ts.replace(minute=0, second=0, microsecond=0)
        return ts


def load_catalog(filename: str) -> dict:
    result = {}
    with open(filename, 'r', encoding='utf-8') as f:
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
            sale[KEY_TS] = iso8601.parse_date(row[COLUMN_TS])
            sale[KEY_PRICE] = float(row[COLUMN_PRICE])
            yield sale


if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
