import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Subhash@123'
)

# Prepare a cursor object
cursorObject = database.cursor()

# Create a database
cursorObject.execute('CREATE DATABASE crmdb')

print('Database created')
