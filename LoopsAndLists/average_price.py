price_list=[]
counter=0
while True:
    try:
        price = float(input("Enter price (or any char to quit):"))
        counter += 1
    except ValueError:
        if counter >= 4:
            break
        print("You need to enter at least 4 prices")
    price_list.append(price)
max_price=max(price_list)
min_price=min(price_list)
if min_price == max_price:
    print("All prices are equal")
else:
    print("The highest price is:%.2f"%max_price)
    print("The lowest price is:%.2f"%min_price)
    price_list.remove(max_price)
    price_list.remove(min_price)
average_list=sum(price_list)/len(price_list)
print("The average price is:%.2f"%average_list)