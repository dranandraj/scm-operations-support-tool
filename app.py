from flask import Flask, render_template, request
from modules.db import get_connection

app = Flask(__name__)

@app.route("/")
def home():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM customers")
    customers_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM materials")
    materials_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM sales_orders")
    sales_orders_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM support_requests")
    support_requests_count = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return render_template(
        "index.html",
        customers_count=customers_count,
        materials_count=materials_count,
        sales_orders_count=sales_orders_count,
        support_requests_count=support_requests_count
    )

@app.route("/customers")
def customers():

    search = request.args.get("search", "").strip()

    connection = get_connection()
    cursor = connection.cursor()

    if search:
        cursor.execute("""
            SELECT customer_id,
                   customer_name,
                   country,
                   status
            FROM customers
            WHERE customer_id ILIKE %s
               OR customer_name ILIKE %s
               OR country ILIKE %s
               OR status ILIKE %s
            ORDER BY customer_id
        """, (
            search,
            search,
            search,
            search
        ))
    else:
        cursor.execute("""
            SELECT customer_id,
                   customer_name,
                   country,
                   status
            FROM customers
            ORDER BY customer_id
        """)

    customers = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "customers.html",
        customers=customers,
        search=search
    )

@app.route("/materials")
def materials():

    search = request.args.get("search", "").strip()

    connection = get_connection()
    cursor = connection.cursor()

    if search:
        cursor.execute("""
            SELECT material_id,
                   material_name,
                   category,
                   plant,
                   price,
                   status
            FROM materials
            WHERE material_id ILIKE %s
               OR material_name ILIKE %s
               OR category ILIKE %s
               OR plant ILIKE %s
               OR status ILIKE %s
            ORDER BY material_id
        """, (
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        ))

    else:
        cursor.execute("""
            SELECT material_id,
               material_name,
               category,
               plant,
               price,
               status
            FROM materials
            ORDER BY material_id
    """)

    materials = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "materials.html",
        materials=materials,
        search=search
    )

@app.route("/sales_orders")
def sales_orders():

    search = request.args.get("search", "").strip()

    connection = get_connection()
    cursor = connection.cursor()

    if search:
        cursor.execute("""
            SELECT order_id,
                   customer_id,
                   material_id,
                   quantity,
                   status,
                   order_date
            FROM sales_orders
            WHERE order_id ILIKE %s
               OR customer_id ILIKE %s
               OR material_id ILIKE %s
               OR status ILIKE %s
            ORDER BY order_id
        """, (
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        ))

    else:
        cursor.execute("""
        SELECT order_id,
               customer_id,
               material_id,
               quantity,
               status,
               order_date
        FROM sales_orders
        ORDER BY order_id
    """)

    sales_orders = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "sales_orders.html",
        sales_orders=sales_orders,
        search=search
    )

@app.route("/support_requests")
def support_requests():

    search = request.args.get("search", "").strip()

    connection = get_connection()
    cursor = connection.cursor()

    if search:
        cursor.execute("""
            SELECT request_id,
                   issue_type,
                   description,
                   status,
                   created_date
            FROM support_requests
            WHERE request_id ILIKE %s
               OR issue_type ILIKE %s
               OR description ILIKE %s
               OR status ILIKE %s
               OR created_date::text ILIKE %s
            ORDER BY request_id
        """, (
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        ))

    else:
        cursor.execute("""
            SELECT request_id,
                   issue_type,
                   description,
                   status,
                   created_date
            FROM support_requests
            ORDER BY request_id
        """)

    support_requests = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "support_requests.html",
        support_requests=support_requests,
        search=search
    )

if __name__ == "__main__":
    app.run(debug=True)