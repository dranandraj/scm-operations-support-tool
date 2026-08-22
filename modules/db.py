import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        port="5433",
        database="scm_support_db",
        user="postgres",
        password="6978"
    )