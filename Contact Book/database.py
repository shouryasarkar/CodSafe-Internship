import pymysql

def create_connection():
    return pymysql.connect(
        host = "localhost",
        user = "root",
        password = "root123",
        database = "contact_book"
    )