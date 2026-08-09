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
# support_requests
# -----------------------------------

for i in range(1, 51):
    request_id = f"SR{i:03d}"
    issue_type = random.choice([
    "Order Error",
    "Customer Master",
    "Material Master",
    "Price Issue",
    "Delivery Delay"
])
    description = random.choice([
    "Customer not found during validation",
    "Material code missing",
    "Incorrect pricing detected",
    "Order processing failed",
    "Delivery date mismatch"
])    
    status = random.choice(["Open", "In Progress", "Resolved", "Closed"])
    created_date = f"2026-05-{random.randint(1, 30):02}"
    cursor.execute(
        """
        INSERT INTO support_requests (request_id, issue_type, description, status, created_date)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (request_id, issue_type, description, status, created_date)
    )

connection.commit()
print("50 Support Requests Inserted")
cursor.close()
connection.close()