import mysql.connector

mydb = mysql.connector.connect(
        host ="localhost",
        user ="root",
        password ="",
        database = "python_db"
)


mycursor = mydb.cursor()

sqlformula = "INSERT INTO student (idstudent,Marks,name,age,lastname) VALUES(%s,%s,%s,%s,%s)"
student1 = (11,99,"Kwaito",25,"Seakamela")

mycursor.execute(sqlformula,student1)

mydb.commit()
