import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C+%t+%h+%w"
    #url = "https://wttr.in/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("No data!")

if __name__ == "__main__":
    city_name = input("City: ")
    weather = get_weather(city_name)
    print(f"The weather in {city_name}: {weather}")
