import mysql.connector



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ineed10^10$",
    database = "testdb"


)
mycursor = mydb.cursor()

##### Create the DATABASE First #####
# mycursor.execute("CREATE DATABASE testdb")

##### Check the DATABASE Whether it is built or not #####
# mycursor.execute("SHOW DATABASES")

 
# for db in mycursor:
#     print(db)


##### Making a Table #####

# mycursor.execute('CREATE TABLE students (name VARCHAR(255), age INTEGER(10))')

#---------- to check the table -------------#

mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)

