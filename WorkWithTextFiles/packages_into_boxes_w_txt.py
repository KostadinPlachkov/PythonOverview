def main():
    try:
        user_input()
    except:
        print("INVALID INPUT")

def user_input():

    width = abs(float(input()))
    height = abs(float(input()))
    depth = abs(float(input()))
    file_name = input()
    min_side_pack, mid_side_pack, max_side_pack = sorted([width, height, depth])
    analyze_data_from_file(max_side_pack, mid_side_pack, min_side_pack, file_name)



def analyze_data_from_file(max_side_pack, mid_side_pack, min_side_pack, file_name):
    with open(file_name, "r", encoding = "utf-8") as f:
        for row in f:
            row = row.strip()
            if row:
                row = row.split(",")
                name = row[0]
                min_side_med, mid_side_med, max_side_med = sorted([float(row[1]), float(row[2]), float(row[3])])
                if max_side_med <= max_side_pack:
                    if mid_side_med <= mid_side_pack:
                        if min_side_med <= min_side_pack:
                            print(name)
                        else:
                            continue
                    else:
                        continue
                else:
                    continue


if __name__ == '__main__':
    main()
