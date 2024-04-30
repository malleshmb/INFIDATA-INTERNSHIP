import mysql.connector

myconn = mysql.connector.connect(
    host = "localhost", user="root",password="",database="company")
cur = myconn.cursor()

try:
    cur.execute("create table employee(ename varchar(30), eid int(4) primary key,dep varchar(20),designation varchar(20),mobile varchar(20),email varchar(20),place varchar(15))")
    print("Your table created successfully")

except Exception as e:
    print("Can not process",e)
myconn.close()