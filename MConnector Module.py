import mysql.connector
from mysql.connector import Error


def MConnector():
    #It creates and returns a connection to MYSQL
    #Can be imported into other programs as a module
    try:
        connection=mysql.connector.connect(host='localhost',user='root',passwd='123sql')
        print('CONNECTION ESTABLISHED')
        return connection
    except Error as e:
        print(f"DATABASE CONNECTION FAILED : {e}")
        return None
MConnector()
    
