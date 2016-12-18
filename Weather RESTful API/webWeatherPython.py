from requests import get
import json
import time
from pprint import pprint
from haversine import haversine
from sense_hat import SenseHat

sense = SenseHat()

stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

my_lat = 38.403342
my_lon = -0.509657

all_stations = get(stations).json()['items']

def find_closest():
    smallest = 20036
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        distance = haversine(my_lon, my_lat, station_lon, station_lat)
        if distance < smallest:
            smallest = distance
            closest_station = station['weather_stn_id']
    return closest_station

closest_stn = find_closest()
    

weather = weather + str(closest_stn)
my_weather = get(weather).json()['items']

temperature = my_weather[0]['ground_temp']
wind = my_weather[0]['wind_speed']
timeOfUpdate = my_weather[0]['updated_on']

sense.show_message('Temp: ' + str(temperature) + "'", text_colour=[255,0,0])
sense.show_message('Wind: ' + str(wind) + "'", text_colour=[0,0,255])
sense.show_message('Act: ' + str(timeOfUpdate) + "'", text_colour=[255,255,0])
