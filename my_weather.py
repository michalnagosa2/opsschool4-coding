import requests
import argparse

access_key = "11c8ce34698da54cf3a042fa67e22516"
weather_url = "http://api.weatherstack.com/current?"

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--celsius', action="store_true")
parser.add_argument('-f', '--fahrenheit', action="store_true")
parser.add_argument('-l', '--cities', nargs='+', required=True)
args = parser.parse_args()

for city in args.cities:
    complete_url = weather_url + "access_key=" + access_key + "&query=" + city
    response = requests.get(complete_url)
    response_in_json_format = response.json()
    weather = response_in_json_format['current']['temperature']
    city = response_in_json_format['location']['name']
    if args.celsius:
        print("the weather of " + city + " is " + str(weather) + "-c")
    elif args.fahrenheit:
        print("the weather of " + city + " is " + str(weather) + "-f")
    if 'error' in response_in_json_format:
        print(response_in_json_format)
