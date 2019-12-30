import requests

access_key = "11c8ce34698da54cf3a042fa67e22516"
weather_url = "http://api.weatherstack.com/current?"
city_name = input("Enter city name : ")
complete_url = weather_url + "access_key=" + access_key + "&query=" + city_name
response = requests.get(complete_url)
response_in_json_format = response.json()

if'error' in response_in_json_format:
    print(response_in_json_format)
else:
    weather = response_in_json_format['current']['temperature']
    city_name = response_in_json_format['location']['name']
    print("the weather of " + city_name + " is " + str(weather) + "-c")