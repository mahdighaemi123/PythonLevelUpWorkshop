import requests

intro = """
------------------------
        Weather
------------------------"""

server = 'http://127.0.0.1:8000'
endpoint = "/get_temp"


def get_temp(city):
    url = server + endpoint + "?city="+city
    response = requests.get(url)
    temp = response.text
    return temp


def main():
    print(intro)
    while 1:
        city = input("> enter your city:")
        temp = get_temp(city)
        print(f"{city} temp is {temp}°C ")


if __name__ == "__main__":
    main()