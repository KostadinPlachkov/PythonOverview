try:
    str_input = str(input())
    str_input = str_input.strip()
    char_dict = dict()
    if str_input:
        for char in str_input:
            if char in char_dict.keys():
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        max_count = max(char_dict.values())
        for key, value in char_dict.items():
            if value == max_count:
                print(key)
    else:
        print("Invalid input")
except:
    print("Invalid input")

