import csv
import os
import sys



def main():
    file_distances = input()
    loading_file_and_calc_result(file_distances)


def loading_file_and_calc_result(file_distances):
    with open(file_distances, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        all_time_intercepts_list = []
        for row in reader:
            starting_intercept = float(row[0])
            ending_intercept = float(row[1])+1
            kmh = float(row[2])
            time = (ending_intercept - starting_intercept) / kmh
            all_time_intercepts_list.append(time)
    whole_time = sum(all_time_intercepts_list)
    print("%.2f" % whole_time)



if __name__ == '__main__':
    try:
        main()
    except:
        print("INVALID INPUT")