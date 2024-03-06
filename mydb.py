#install mysql 
# >pip install mysqlclient
#or  >pip install pymysql
#and add code inside project folder(message)
    #import pymysql
    #pymysql.install_as_MySQLdb()
# >pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root'
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE crmapp")

print("All Done!")

# >python mydb.py
#check mysql workbench -- database is created
# >python manage.py migrate
#check different tables are created

#TO CREATE SUPER USER
# >python manage.py createsuperuser
#Username: admin
#Email: shwetachavan612@gmail.com
#password: pooja612
#Superuser created successfully