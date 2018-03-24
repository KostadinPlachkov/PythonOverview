"""
2
./containers.txt
"""

from math import pi
import csv
import operator

try:
    liters = float(input())
    file_name = input()

    name_volume_dict = {}
    with open(file_name, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        for row in reader:

            if row:
                name_of_container = row[0]
                radius = float(row[1]) / 10
                height = float(row[2]) / 10
                current_volume = pi * radius ** 2 * height
                if liters <= current_volume:
                    name_volume_dict[name_of_container] = current_volume
                else:
                    continue
            else:
                continue
    if name_volume_dict:
        sorted_name_volume = min(name_volume_dict.items(), key = operator.itemgetter(1))
        print(sorted_name_volume[0])
    else:
        print("NO SUITABLE CONTAINER")
except:
    print("INVALID INPUT")
