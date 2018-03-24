"""
fridge-temp.txt
"""


import csv


file_name = input()
data_list = []
with open(file_name, "r", encoding = "utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        data_list.append([row[0], float(row[1])])

prev_temp = 0
for row in data_list:
    if data_list[0] == row and row[1] > 10:
        print(row[0])
    elif data_list[0] == row:
        prev_temp = row[1]
    else:
        current_temp = row[1]
        if current_temp > prev_temp + 4:
            print(row[0])
            prev_temp = current_temp
        else:
            prev_temp = current_temp
            continue
