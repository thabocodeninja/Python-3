import mysql.connector


mydb = mysql.connector.connect(
        host ="localhost",
        user = "root",
        password ="",
        database ="python_db"

)

mycursor = mydb.cursor()
sql = "SELECT * FROM student where name = 'ntwana'"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for result in myresult:
        print(result)