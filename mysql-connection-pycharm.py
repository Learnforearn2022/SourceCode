import mysql.connector

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="#Learnforearn2022#",
    database="dbo"
)

if con:
    print("connected")
else:
    print("nope")

mycursor = con.cursor()

mycursor.execute('select * from persons')

persons = mycursor.fetchall()

for person in persons:
    print(person)