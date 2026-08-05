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
# Materials
# -----------------------------------

for i in range(1, 51):

    material_id = f"M{i:03}"
    material_name = f"Material {i}"
    category = random.choice(["Electronics", "Hardware", "Software", "Networks", "Accessories"])
    plant = random.choice(["JP01", "IN01", "US01", "GR01", "SG01"])
    price = random.randint(100, 5000)
    status = random.choice(["Available", "Out of Stock"])
    cursor.execute(
        """
        INSERT INTO materials (material_id, material_name, category, plant, price, status) VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (material_id, material_name, category, plant, price, status)
    )

connection.commit()
print("50 Materials Inserted")
cursor.close()
connection.close()