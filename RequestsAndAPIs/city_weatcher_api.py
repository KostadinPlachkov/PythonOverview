from pprint import pprint
import requests
from datetime import datetime
import pytz




def main():
    APPID = "965acdac1ae64cf06761bb563ad34d96"

    URL_API = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=" + APPID
    URL_API_SET = user_input(URL_API)
    getting_data(URL_API_SET)


def user_input(URL_API):
    city = str(input("Въведете град:"))
    return URL_API.format(city)

def getting_data(URL_API_SET):
    try:
        response = requests.get(URL_API_SET, timeout=20)
        if response.status_code == 200:
            weather_data = response.json()
            dt = weather_data["dt"]
            temp_k = weather_data["main"].get("temp")
            temp_c = float(temp_k - 273.15)
            pressure = weather_data["main"].get("pressure")
            humidity = weather_data["main"].get("humidity")
            wind = weather_data["wind"].get("speed")
            printing_data(dt, temp_c, pressure, humidity, wind)

        else:
            print("Error from server:", response.status_code)
    except Exception as e:
        print("Error from server!", str(e))

def printing_data(dt, temp_c, pressure, humidity, wind):

    print("Информация към:", datetime.utcfromtimestamp(dt))
    print("Температура: %.2f" % temp_c)
    print("Налягане:", pressure)
    print("Влажност: {}%".format(humidity))
    print("Вятър: {} м/с".format(wind))


if __name__ == '__main__':
    main()

