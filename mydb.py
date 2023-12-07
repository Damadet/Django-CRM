import mysql.connector

try:
    dataBase = mysql.connector.connect(
        host = 'localhost',
        user = 'damadet',
        passwd = 'damadet1'
    )

    #prepare a cursor object
    cursorObject = dataBase.cursor()

    #create a database
    cursorObject.execute("CREATE DATABASE elderco")

    print("All Done!")

except mysql.connector.Error as err:
        print(f"Error: {err}")

