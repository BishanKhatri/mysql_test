import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ineed10^10$",
    database = "testdb"
)

mydatabase = mydb.cursor()

mydatabase.execute("SELECT age FROM students")

result = mydatabase.fetchone()

for row in result:
    print(row)