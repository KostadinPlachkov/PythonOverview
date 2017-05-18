import iso8601
from datetime import datetime, date, timedelta
import calendar
import csv

csv_file = "sales.csv"
COLUMN_PRICE = 1
COLUMN_DAYTIME = 0


def calc_income_by_hours(csv_file):
    income_per_hour_dict = {}
    with open(csv_file, encoding = "utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            price = float(row[COLUMN_PRICE])
            day_str = row[COLUMN_DAYTIME]
            dt_obj = iso8601.parse_date(day_str)
            hour = dt_obj.strftime("%H")
            if hour in income_per_hour_dict:
                income_per_hour_dict[hour] += price
            else:
                income_per_hour_dict[hour] = price
        max_income_hour = max(income_per_hour_dict, key = income_per_hour_dict.get)
        print("The highest income is between {}:00 and {}:00: {} ".format(max_income_hour, int(max_income_hour) + 1, income_per_hour_dict[max_income_hour]))

def calc_max_income_by_dt(csv_file):
    week = {}
    with open(csv_file, encoding = "utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            day_str = row[COLUMN_DAYTIME]
            day_obj = iso8601.parse_date(day_str)
            price = float(row[COLUMN_PRICE])
            current_day = calendar.day_name[day_obj.weekday()]
            if current_day in week:
                week[current_day] += price
            else:
                week[current_day] = price
    for day, income in week.items():
        print("Income on", day, ": %.2f" % income)
    max_day_income = max(week, key = week.get)
    print("The highest income is on", max_day_income, ": %.2f" % week[max_day_income])

if __name__ == '__main__':
    calc_max_income_by_dt(csv_file)
    calc_income_by_hours(csv_file)
