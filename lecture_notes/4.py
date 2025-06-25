<<<<<<< HEAD
'''#csv filesAdd commentMore actions
=======

'''#csv files
>>>>>>> a9e740445df3aafb6b8ce9e5e6f170108e776f10
import csv
data = [["Name","Age","Country"],["A","10","India"],["B","19","Aus"],["C","23","Jpn"]]
with open ("data.csv","w",newline="") as file:
    writer = csv.writer(file)
    for i in data:
        writer.writerow(i)

with open("data.csv","r") as file:
     reader = csv.reader(file)
     for i in reader:
         print(i)

try:
    n = int(input("Enter any no "))
    y = 25/n
    print(y)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Invalid Input! Required a Number")

import requests
def weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ba1f90aaa6f5c0a7edb61878f538fd0f"
    try:
        response  = requests.get(url)
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        feels_like = data["main"]["feels_like"]
        print(f"Weather in {city}:")
        print(f"Temperature {(temperature-273.15):.2f} C")
        print(f"Humidity {humidity}")
        print(f"Feels like {(feels_like-273.15):.2f} C")
        print(f"Description {data["weather"][0]["description"].capitalize()}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
city = input("Enter city: ")
weather(city)

import sqlite3
conn = sqlite3.connect("db1.db")'''
'''conn.execute("""
Create table Users(
userid INTEGER PRIMARY KEY AUTOINCREMENT,
user VARCHAR(50),
pass VARCHAR(20),
mobile VARCHAR(50),
email VARCHAR(50)
)""")


conn.execute("""
INSERT INTO USERS VALUES (1,'A','a','ab','abc'),(2,'B','b','bc','bcd'),(3,'C','c','cd','cde'),(4,'D','d','de','def')
""")
conn.commit()


data = conn.execute("""
SELECT * FROM USERS
""")
for i in data:
    print(i)

id = int(input("Enter no "))
conn.execute("DELETE FROM USERS WHERE USERID =?",(id,))
conn.commit()

conn.execute("UPDATE USERS SET USER = 'X' WHERE USERID = 1")
conn.commit()

data = conn.execute("""
SELECT * FROM USERS ORDER BY USER DESC LIMIT  2 
""")

for i in data:
    print(i)
conn.close()
'''
import pywhatkit
pywhatkit.sendwhatmsg('+919887856202','hello isha',17,48)