import mysql.connector
try:
    mydb = mysql.connector.connect(
        host="localhost",
        port=3307,
        user="root",
        password="",
        database="khushi_db",
        use_pure=True,
    )

    mycursor = mydb.cursor()
except mysql.connector.Error as err:
    print("Database Connection Error:", err)
    exit()