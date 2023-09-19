import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ineed10^10$",
    database = "testdb"
)

mydatabase = mydb.cursor()

#--------Inster the data inside the table --------------#

# --- first make the formula ----------#

sql_formula = "INSERT INTO students(name, age) VALUES(%s, %s)"
students = [
    ("Ram",25),
    ("rohit",23),
    ("sita",27),
    ("hari",24),
    ("Shyam",22),
]

mydatabase.executemany(sql_formula, students)

mydb.commit()