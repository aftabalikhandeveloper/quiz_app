import mysql.connector


def get_connection():
    # Connect to server
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="",
        database="quiz_app"
        )
    
