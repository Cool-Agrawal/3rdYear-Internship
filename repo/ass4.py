
#ques 1
import csv
data = [["Name","Address","Mobile","Email"],["A","Sector 5","9812742043","abc@gmail.com"],["B","Sector 9","9128302245","bcd2gmail.com"],["C","Sector 8","9618233640","cde@gmail.com"]]
with open ("address_book.csv","w",newline="") as file:
    writer = csv.writer(file)
    for i in data:
        writer.writerow(i)

with open("address_book.csv","r") as file:
     reader = csv.reader(file)
     for i in reader:
         print(i)
#ques 2
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


#ques 3
import sqlite3
conn = sqlite3.connect("ass.db")

conn.execute("""
Create table User(
u_id INTEGER PRIMARY KEY AUTOINCREMENT,
f_name VARCHAR(20),
l_name VARCHAR(20),
u_no INTEGER
);""")
conn.execute("""
Create table Product(
p_id INTEGER PRIMARY KEY AUTOINCREMENT,
p_name varchar(20),
price INTEGER
);
""")
conn.execute("""
Create table Quantity(
q_id INTEGER PRIMARY KEY AUTOINCREMENT,
q_name varchar(20),
q_no INTEGER
)
""")


conn.execute("""
INSERT INTO USER VALUES (1,'a','A',100),(2,'b','B',200),(3,'c','C',300),(4,'d','D',400)
""")
conn.execute("""
INSERT INTO PRODUCT VALUES (1,'a',1000),(2,'b',2000),(3,'c',3000),(4,'d',4000)
""")
conn.execute("""
INSERT INTO quantity VALUES (1,'q1',12),(2,'q2',20),(3,'q3',13),(4,'q4',40)
""")
conn.commit()


u_data = conn.execute("""
SELECT * FROM USER
""")
p_data = conn.execute("""
SELECT * FROM PRODUCT
""")
q_data = conn.execute("""
SELECT * FROM QUANTITY
""")
for i in u_data:
    print(i)
for i in p_data:
    print(i)
for i in q_data:
    print(i)

id = int(input("Enter no "))
conn.execute("DELETE FROM USER WHERE U_ID =?",(id,))
conn.execute("DELETE FROM PRODUCT WHERE P_ID =?",(id,))
conn.execute("DELETE FROM QUANTITY WHERE Q_ID =?",(id,))


conn.commit()

conn.execute("UPDATE USER SET F_NAME = 'X' WHERE U_ID = 1")
conn.execute("UPDATE PRODUCT SET P_NAME = 'Y' WHERE p_ID = 1")
conn.execute("UPDATE QUANTITY SET Q_NAME = 'Z' WHERE q_ID = 1")

conn.commit()

u_data = conn.execute("""
SELECT * FROM USER
""")
p_data = conn.execute("""
SELECT * FROM PRODUCT
""")
q_data = conn.execute("""
SELECT * FROM QUANTITY
""")
for i in u_data:
    print(i)
for i in p_data:
    print(i)
for i in q_data:
    print(i)


conn.close()
