from bs4 import BeautifulSoup
import requests

url = "https://pogoda.interia.pl/"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
print ("Choose a place and find out what the temperature is there: ")
x=0
cities = []
weathers = []
while x<23:
    city = doc.find_all("a", {"class": "weather-index-item-name saveCityInCookie"})[x]
    weather = doc.find_all("span", {"class": "weather-index-item-temp"})[x]

    cityStrip = city.string.strip()
    weatherToArray = weather.string
    cities.append(cityStrip)
    weathers.append(weatherToArray)
    print(city.string.strip()," ", end = '')
    x=x+1
print("")
whatCity = input()

x=0
while(x<23):
    if(whatCity.lower()==cities[x].lower()):
        print(cities[x], weathers[x])
    x=x+1



