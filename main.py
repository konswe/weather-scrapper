from bs4 import BeautifulSoup
import requests
import pymysql
from datetime import date

url = "https://pogoda.interia.pl/"

date = date.today().strftime("%Y-%m-%d")

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
print ("Choose a place and find out what the temperature is there: ")
x=0
cities = []
weathers = []


#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="weather")
cursor = connection.cursor()

# queries for retrievint last date
retrive = "SELECT Date FROM `weather_database` ORDER BY `weather_database`.`Date` DESC"

#initiating date its required if there is no last date
lastDate = "1700-01-01"

#executing the quires
cursor.execute(retrive)
#checks if there is anything in the database
if cursor.execute(retrive) != 0:
    lastDate = cursor.fetchall()[0]
    lastDate = lastDate[0].strftime('20%y-%m-%d')



while x<23:
    city = doc.find_all("a", {"class": "weather-index-item-name saveCityInCookie"})[x]
    weather = doc.find_all("span", {"class": "weather-index-item-temp"})[x]

    #making data more readable
    cityStrip = city.string.strip()
    weatherToArray = weather.string

    #this if is becouse we dont want thisame data in database
    if lastDate != date:
        #SQL
        insert1 = ("INSERT INTO weather_database(City, Weather, Date) "
                   "VALUES (%(city)s,%(weather)s,%(date)s)")

        data_weather = {
            'city': cityStrip,
            'weather': weatherToArray.strip(),
            'date': date,
        }

        # executing the quires
        cursor.execute(insert1, data_weather)

    cities.append(cityStrip)
    weathers.append(weatherToArray)
    print(city.string.strip()," ", end = '')
    x=x+1

#ending SQL connection and commiting changes
connection.commit()
connection.close()

print("")
whatCity = input()

x=0

#printing out weather of the city input
while(x<23):
    if(whatCity.lower()==cities[x].lower()):
        print(cities[x], weathers[x])
    x=x+1





