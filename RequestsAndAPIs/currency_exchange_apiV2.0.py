import requests
from datetime import datetime


URL_API = "http://api.fixer.io/{date}?base={from_currency}&symbols={to_currency}"


def main():

    user_input()



def user_input():
    print("Конвертор на валути")
    date = str(input("Въведете дата [yyyy-mm-dd]:"))
    if not date:
        date = "latest"
    base_currency = str(input("Въведете валута:")).upper()
    money = float(input("Въведете сума:"))
    to_currency = str(input("Въведете валута, към която да се конвертира:")).upper()
    URL_API_SET = URL_API.format(date = date, from_currency = base_currency, to_currency = to_currency)

    getting_currency_exchange(URL_API_SET, money, to_currency)


def getting_currency_exchange(URL_API_SET, user_money, to_currency):
    try:
        response = requests.get(URL_API_SET, timeout=20)
        if response.status_code == 200:
            exchange_rates = response.json()
            rate = exchange_rates.get("rates", {})
            currency_rate = rate.get(to_currency, None)
            if not currency_rate:
                print("NO DATA")
            exchanged_money = user_money * currency_rate
            print("Равностойност в {}: {:.2f}".format(to_currency, exchanged_money))
        else:
            print("Error from server:", response.status_code)
    except Exception as e:
        print("Error from server!", str(e))

if __name__ == '__main__':
    main()