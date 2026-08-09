import psycopg2
import random

random.seed(42)

connection = psycopg2.connect(
    host="localhost",
    port="5432",
    database="scm_support_db",
    user="postgres",
    password="6978"
)

cursor = connection.cursor()

# -----------------------------------
# Customers
# -----------------------------------

for i in range(1, 51):

    customer_id = f"C{i:03d}"
    customer_name = f"Customer {i}"
    country = random.choice(["Japan", "India", "USA", "Germany", "Singapore"])
    status = random.choice(["Active", "Inactive"])
    cursor.execute(
        """
        INSERT INTO customers (customer_id, customer_name, country, status)
        VALUES (%s, %s, %s, %s)
        """,
        (customer_id, customer_name, country, status)
    )

connection.commit()
print("50 Customers Inserted")
cursor.close()
connection.close()