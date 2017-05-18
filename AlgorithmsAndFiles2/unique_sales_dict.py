"""
sales.txt
"""
import csv


try:
    file_name = input()
    id_city_dict = {}
    with open(file_name, "r", encoding = "utf-8") as f:
        for row in f:
            row = row.strip()
            if row:
                row = row.split(",")
                item_id = row[0]
                item_id = item_id[1:-1]
                city = row[2]
                city = city[1:-1]
                if item_id in id_city_dict.keys():
                    id_city_dict[item_id].append(city)
                else:
                    id_city_dict[item_id] = [city]
            else:
                continue
    # print(id_city_dict)
    unique_sales = {}
    for item_id, city_list in id_city_dict.items():
        if len(city_list) == 1:
            city = city_list[0]
            if city in unique_sales.keys():
                unique_sales[city].append(item_id)
            else:
                unique_sales[city] = [item_id]
    # print(unique_sales)
    if unique_sales:
        unique_sales = sorted(unique_sales.items())
        for city, item_id in unique_sales:
            # print(city, item_id)
            item_id = sorted(item_id)
            for item in item_id:
                # print(item)
                city += "," + item
            print(city)
    else:
        print("NO UNIQUE SALES")
except:
    print("INVALID INPUT")