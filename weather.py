import pymysql

#database connection
connection = pymysql.connect(host="localhost", user="root", passwd="", database="weather")
cursor = connection.cursor()

# queries for retrievint all rows
retrive = "SELECT Date FROM `weather_database` ORDER BY `weather_database`.`Date` DESC"

#executing the quires
cursor.execute(retrive)
lastDate = cursor.fetchall()[0]
lastDate = lastDate[0].strftime('20%y-%m-%d')
print(lastDate)



#commiting the connection then closing it.
connection.commit()