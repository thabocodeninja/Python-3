import mysql.connector


mydb = mysql.connector.connect(

        host= "localhost",
        user = "root",
        password = "",
        database = "python_db"
)

mycursor = mydb.cursor()


sql = "UPDATE student SET age = 20 where name = 'thabo'"

mycursor.execute(sql)

mydb.commit()



