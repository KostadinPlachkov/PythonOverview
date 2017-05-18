import csv

KEY_PRICE = ['key_price']
KEY_CITY = ['key_city']
KEY_ID = ['key_id']

COLUMN_PRICE = -1
COLUMN_CITY = 2
COLUMN_ID = 0



def main():
    user_input()

def user_input():
    item_id = input()
    file_name = input()
    loading_file_and_calc_data(item_id, file_name)



def loading_file_and_calc_data(item_id, file_name):

    city_list = []
    price_list = []
    with open(file_name, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        for row in reader:

            if row[COLUMN_ID] == item_id:
                city_list.append(row[COLUMN_CITY])
                price_list.append(row[COLUMN_PRICE])
            else:
                continue
    index_city = price_list.index(min(price_list))
    # print(index_city)
    print(*city_list[index_city:index_city+1])



if __name__ == '__main__':
    try:
        main()
    except:
        print("INVALID INPUT")