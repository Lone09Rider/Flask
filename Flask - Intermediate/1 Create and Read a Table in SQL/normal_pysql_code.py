from pymysql import DatabaseError
import pymysql

try:
    con = pymysql.connect(
        host="localhost", 
        user="root", 
        password="root", 
        database="my_flask"
        )
    #Create DB
    # sql = "CREATE DATABASE IF NOT EXISTS my_flask"
    # con.cursor().execute(sql)
    # con.commit()
    
    # Create Table
    # sql = "CREATE TABLE Movies(id INTEGER AUTO_INCREMENT PRIMARY KEY, name varchar(30), rating varchar(20))"
    # con.cursor().execute(sql)
    # con.commit()
    
    # INSERT DATA
    print("Successfully Conneted!!")
    con.close()
except DatabaseError as e:
    print("Some error!! : ", e)
    
