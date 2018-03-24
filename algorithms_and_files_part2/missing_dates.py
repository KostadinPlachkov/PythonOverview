"""
city-temperature-data.txt
"""

import csv
import operator
from datetime import date, timedelta, datetime


file_name = input()
city_dict = {}
with open(file_name, "r", encoding = "utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        if row:
            city = row[1]
            date = datetime.strptime(row[0], "%Y-%m-%d")
            # print(date)

            if city in city_dict.keys():
                city_dict[city].append(date)
            else:
                city_dict[city] = [date]
# print(city_dict)
ending_date = max(city_dict.items(), key = operator.itemgetter(1))[1][0]
starting_date = min(city_dict.items(), key = operator.itemgetter(1))[1][0]
# print(ending_date)
horological_list = sorted(city_dict.items(), key = operator.itemgetter(1))
max_days = sorted(city_dict.items(), key = operator.itemgetter(1))[::-1]
max_days_set = set(max_days[0][1])
# print(horological_list)
for city, date_list in horological_list:
    missing = max_days_set - set(date_list)
    missing = sorted(missing)
    if missing:
        for date in missing:
            print(city, date)
