destin_name = "catalog_sample.csv"
with open(destin_name, encoding = "utf-8") as f:
    prices = []
    for line in f:
        line = line.strip()
        words_in_line_list = line.split(",")
        prices.append(float(words_in_line_list[6]))
    average_price = sum(prices) / len(prices)
    print("The average price is:%.2f" % average_price)
