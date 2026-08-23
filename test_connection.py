import psycopg2
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

try:
    connection = psycopg2.connect(
        host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD
    )

    print("Database Connected Successfully!")
    connection.close()

except Exception as error:
    print("Connection Failed")
    print(error)
