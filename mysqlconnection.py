import mysql.connector

def getAddress(longitude, latitude):
    # MySQL connection created
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Anan14957154792",
        database="project_1"
    )

    # MySQL connection check
    if mydb.is_connected():
        print("Bağlantı başarılı!")

    # Create cursor
    mycursor = mydb.cursor()

    # query example
    mycursor.execute("SELECT * FROM mahallerler WHERE Longitude_1 <= %s AND Longitude_end >= %s AND Latitude_1 <= %s AND Latitude_end >= %s", 
                     (longitude, longitude, latitude, latitude))

    # got whole data
    records = mycursor.fetchall()

    return records

longitude = 28.85241000
latitude =  40.99657500
mahalleler = getAddress(longitude, latitude)
print(mahalleler)
