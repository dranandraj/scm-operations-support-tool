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
# Sales Orders
# -----------------------------------

for i in range(1, 101):

    order_id = f"SO{i:03}"
    customer_id = f"C{random.randint(1, 50):03}"
    material_id = f"M{random.randint(1, 50):03}"
    quantity = random.randint(1, 100)
    status = random.choice(["Pending", "Shipped", "Delivered", "Cancelled"])
    cursor.execute(
        """
        INSERT INTO sales_orders (order_id, customer_id, material_id, quantity, status)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (order_id, customer_id, material_id, quantity, status)
    )

connection.commit()
print("100 Sales Orders Inserted")
cursor.close()
connection.close()