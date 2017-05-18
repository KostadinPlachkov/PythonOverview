import requests

BASE_CURRENCY = "BGN"


def main():
    URL_API_LATEST = "http://api.fixer.io/latest?base={}&symbols=".format(BASE_CURRENCY)

    URL_API_LATEST_SET, money, user_currency = user_input(URL_API_LATEST)
    getting_user_currency_to_bg(URL_API_LATEST_SET, money, user_currency)



def user_input(URL_API_LATEST):
    print("Конвертор на валути към български лева.")
    currency = str(input("Въведете валута:")).upper()
    money = float(input("Въведете сума:"))
    URL_API_LATEST_SET = URL_API_LATEST+currency
    return URL_API_LATEST_SET, money, currency


def getting_user_currency_to_bg(URL_API_LATEST_SET, user_money, user_currency):
    try:
        response = requests.get(URL_API_LATEST_SET, timeout=20)
        if response.status_code == 200:
            exchange_rates = response.json()
            rate = exchange_rates.get("rates", {})
            currency_perc = rate.get(user_currency, None)
            if not currency_perc:
                print("NO DATA")
            bgn_money = user_money / currency_perc
            print("Равностойност в BGN: %.2f" % bgn_money)
        else:
            print("Error from server:", response.status_code)
    except Exception as e:
        print("Error from server!", str(e))

if __name__ == '__main__':
    main()