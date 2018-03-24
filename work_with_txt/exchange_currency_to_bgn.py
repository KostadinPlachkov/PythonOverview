def main():
    exchange_file = input()
    amounts_file = input()
    loading_files(exchange_file, amounts_file)


def loading_files(exchange_file, amounts_file):
    with open(exchange_file, "r", encoding = "utf-8") as fe:
        exchange_dict = {}
        for row in fe:
            row = row.strip()
            if row:
                row = row.split(" ")
                exchange_dict[row[0]] = float(row[1])
            else:
                continue

    with open(amounts_file, "r", encoding = "utf-8") as fa:
        amounts_list = []
        for row in fa:
            row = row.strip()
            if row:
                row = row.split(" ")
                amounts_list.append([row[1], float(row[0])])
            else:
                continue
    calc_exchange(exchange_dict, amounts_list)


def calc_exchange(exchange_list, amounts_list):
    for exchange in amounts_list:

        if exchange[0] in exchange_list.keys():
            rate = exchange[1] / exchange_list[exchange[0]]
            print("{:.2f}".format(rate))

        else:
            continue



if __name__ == '__main__':
    try:
        main()
    except:
        print("INVALID INPUT")
