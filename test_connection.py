import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        database="scm_support_db",
        user="postgres"
    )

    print("Database Connected Successfully!")

    connection.close()

except Exception as error:
    print("Connection Failed")
    print(error)