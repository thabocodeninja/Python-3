import mysql.connector



mydb = mysql.connector.connect(
       host = "localhost",
       user = "root",
       password = "",
       database = "python_db"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM student ORDER BY age"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for r in myresult:

     print(r)
