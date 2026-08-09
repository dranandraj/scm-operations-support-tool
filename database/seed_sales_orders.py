import psycopg2
import random
from datetime import date, timedelta

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

    order_id = f"SO{i:03d}"
    customer_id = f"C{random.randint(1, 50):03d}"
    material_id = f"M{random.randint(1, 50):03d}"
    quantity = random.randint(1, 100)
    status = random.choice(["Pending", "Shipped", "Delivered", "Cancelled"])
    order_date = date.today() - timedelta(days=random.randint(0, 180))
    cursor.execute(
        """
        INSERT INTO sales_orders (order_id, customer_id, material_id, quantity, status, order_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (order_id, customer_id, material_id, quantity, status, order_date)
    )

connection.commit()
print("100 Sales Orders Inserted")
cursor.close()
connection.close()