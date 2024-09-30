import requests

OWM_Enpoint="https://api.openweathermap.org/data/2.5/weather"
api_key="e307eeb036c71c62c9865d7899994c99"

weather_params= {
    "lat":21.170240,
    "lon":72.831062,
    "appid":api_key,
    "cnt":4,
}
response=requests.get(OWM_Enpoint,params=weather_params)
response.raise_for_status()
weather_data=response.json()
print(weather_data)