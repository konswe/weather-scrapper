import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="weather")
cursor = connection.cursor()

city = "katoddwice"
weather = "19C"
date = "9929-12-31"

# queries for inserting values
insert1 = ("INSERT INTO weather_database(City, Weather, Date) " 
          "VALUES (%(city)s,%(weather)s,%(date)s)")


data_weather = {
  'city': city,
  'weather': weather,
  'date': date,
}


#executing the quires
cursor.execute(insert1, data_weather)


#commiting the connection then closing it.
connection.commit()
connection.close()