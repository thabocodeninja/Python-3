import mysql.connector


mydb = mysql.connector.connect(
    hostname = "localhost"
    user = "root",
    password = ""
)
mycursor = mydb.cursor()

sql = "Delete From student where name = "mike"
mycursor .execute(sql)

mydb.commit()


