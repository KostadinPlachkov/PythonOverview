destination_name = "catalog_full.csv"

with open(destination_name, encoding = "utf-8") as f:
    prices_man = []
    prices_woman = []
    prices_kid = []
    prices_infant = []
    for line in f:
        line = line.strip()
        words_in_line_list = line.split(",")
        if words_in_line_list[5] == "Men" or words_in_line_list[5] == "Unisex":
            prices_man.append(float(words_in_line_list[6]))
        elif words_in_line_list[5] == "Woman" or words_in_line_list[5] == "Unisex":
            prices_woman.append(float(words_in_line_list[6]))
        elif words_in_line_list[5] == "Kid":
            prices_kid.append(float(words_in_line_list[6]))
        elif words_in_line_list[5] == "Infant":
            prices_infant.append(float(words_in_line_list[6]))
    average_price_M = sum(prices_man) / len(prices_man)
    average_price_W = sum(prices_woman) / len(prices_woman)
    average_price_K = sum(prices_kid) / len(prices_kid)
    average_price_I = sum(prices_infant) / len(prices_infant)
    print("The average price for Men is:%.2f" % average_price_M)
    print("The average price for Women is:%.2f" % average_price_W)
    print("The average price for Kids is:%.2f" % average_price_K)
    print("The average price for Infants is:%.2f" % average_price_I)