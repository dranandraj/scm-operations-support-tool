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
    country = request.args.get("country", "").strip()
    status = request.args.get("status", "").strip()

    sort_by = request.args.get("sort_by", "customer_id")
    sort_order = request.args.get("sort_order", "asc")

    # Pagination
    page = request.args.get("page", 1, type=int)
    per_page = 10

    if page < 1:
        page = 1

    # Allowed columns for sorting
    sort_options = {
        "customer_id": "customer_id",
        "customer_name": "CAST(REGEXP_REPLACE(customer_name, '[^0-9]', '', 'g') AS INTEGER)",
        "country": "country",
        "status": "status"
    }

    order_column = sort_options.get(sort_by, "customer_id")

    order_direction = "DESC" if sort_order == "desc" else "ASC"

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT customer_id,
               customer_name,
               country,
               status
        FROM customers
        WHERE 1=1
    """

    params = []

    # Search
    if search:
        query += """
            AND (
                customer_id ILIKE %s
                OR customer_name ILIKE %s
                OR country ILIKE %s
                OR status ILIKE %s
            )
        """

        params.extend([
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        ])

    # Country filter
    if country:
        query += " AND country = %s"
        params.append(country)

    # Status filter
    if status:
        query += " AND status = %s"
        params.append(status)

    # Count filtered records
    count_query = """
        SELECT COUNT(*)
        FROM customers
        WHERE 1=1
    """

    count_params = []

    if search:
        count_query += """
            AND (
                customer_id ILIKE %s
                OR customer_name ILIKE %s
                OR country ILIKE %s
                OR status ILIKE %s
            )
        """

        count_params.extend([
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        ])

    if country:
        count_query += " AND country = %s"
        count_params.append(country)

    if status:
        count_query += " AND status = %s"
        count_params.append(status)

    cursor.execute(count_query, count_params)

    total_records = cursor.fetchone()[0]

    # Calculate total pages
    total_pages = max(1, (total_records + per_page - 1) // per_page)

    # Prevent invalid page number
    if page > total_pages:
        page = total_pages

    offset = (page - 1) * per_page

    # Sorting + Pagination
    query += f"""
        ORDER BY {order_column} {order_direction}
        LIMIT %s OFFSET %s
    """

    params.extend([per_page, offset])

    cursor.execute(query, params)

    customers = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "customers.html",
        customers=customers,
        search=search,
        country=country,
        status=status,
        sort_by=sort_by,
        sort_order=sort_order,
        page=page,
        per_page=per_page,
        total_records=total_records,
        total_pages=total_pages
    )

@app.route("/materials")
def materials():

    search = request.args.get("search", "").strip()
    category = request.args.get("category", "").strip()
    plant = request.args.get("plant", "").strip()
    status = request.args.get("status", "").strip()

    sort_by = request.args.get("sort_by", "material_id")
    sort_order = request.args.get("sort_order", "asc")

    # Pagination
    page = request.args.get("page", 1, type=int)
    per_page = 10
    offset = (page - 1) * per_page

    # Allowed columns for sorting
    sort_options = {
        "material_id": "material_id",
        "material_name": "CAST(REGEXP_REPLACE(material_name, '[^0-9]', '', 'g') AS INTEGER)",
        "category": "category",
        "plant": "plant",
        "price": "price",
        "status": "status"
    }

    # Prevent invalid column names
    order_column = sort_options.get(sort_by, "material_id")

    # Only allow ASC / DESC
    order_direction = "DESC" if sort_order == "desc" else "ASC"

    connection = get_connection()
    cursor = connection.cursor()

    # -----------------------------------
    # Total records count
    # -----------------------------------

    count_query = """
        SELECT COUNT(*)
        FROM materials
        WHERE 1=1
    """

    count_params = []

    # Search
    if search:
        count_query += """
            AND (
                material_id ILIKE %s
                OR material_name ILIKE %s
                OR category ILIKE %s
                OR plant ILIKE %s
                OR status ILIKE %s
            )
        """

        count_params.extend([
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        ])

    # Category filter
    if category:
        count_query += " AND category = %s"
        count_params.append(category)

    # Plant filter
    if plant:
        count_query += " AND plant = %s"
        count_params.append(plant)

    # Status filter
    if status:
        count_query += " AND status = %s"
        count_params.append(status)

    cursor.execute(count_query, count_params)

    total_count = cursor.fetchone()[0]

    # -----------------------------------
    # Main query
    # -----------------------------------

    query = """
        SELECT material_id,
               material_name,
               category,
               plant,
               price,
               status
        FROM materials
        WHERE 1=1
    """

    params = []

    # Search
    if search:
        query += """
            AND (
                material_id ILIKE %s
                OR material_name ILIKE %s
                OR category ILIKE %s
                OR plant ILIKE %s
                OR status ILIKE %s
            )
        """

        params.extend([
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        ])

    # Category filter
    if category:
        query += " AND category = %s"
        params.append(category)

    # Plant filter
    if plant:
        query += " AND plant = %s"
        params.append(plant)

    # Status filter
    if status:
        query += " AND status = %s"
        params.append(status)

    # Sorting
    query += f" ORDER BY {order_column} {order_direction}"

    # Pagination
    query += " LIMIT %s OFFSET %s"

    params.extend([per_page, offset])

    cursor.execute(query, params)

    materials = cursor.fetchall()

    # Calculate total pages
    total_pages = (total_count + per_page - 1) // per_page

    cursor.close()
    connection.close()

    return render_template(
        "materials.html",
        materials=materials,
        search=search,
        category=category,
        plant=plant,
        status=status,
        sort_by=sort_by,
        sort_order=sort_order,
        page=page,
        total_pages=total_pages
    )

@app.route("/sales_orders")
def sales_orders():

    search = request.args.get("search", "").strip()
    status = request.args.get("status", "").strip()

    sort_by = request.args.get("sort_by", "order_id")
    sort_order = request.args.get("sort_order", "asc")

    # Pagination
    page = request.args.get("page", 1, type=int)
    per_page = 10
    offset = (page - 1) * per_page

    # Allowed columns for sorting
    sort_options = {
        "order_id": "order_id",
        "customer_id": "customer_id",
        "material_id": "material_id",
        "quantity": "quantity",
        "status": "status",
        "order_date": "order_date"
    }

    # Prevent invalid column names
    order_column = sort_options.get(sort_by, "order_id")

    # Only allow ASC / DESC
    order_direction = "DESC" if sort_order == "desc" else "ASC"

    connection = get_connection()
    cursor = connection.cursor()

    # -----------------------------------
    # Total records count
    # -----------------------------------

    count_query = """
        SELECT COUNT(*)
        FROM sales_orders
        WHERE 1=1
    """

    count_params = []

    # Search
    if search:
        count_query += """
            AND (
                order_id ILIKE %s
                OR customer_id ILIKE %s
                OR material_id ILIKE %s
                OR status ILIKE %s
                OR order_date::text ILIKE %s
            )
        """

        count_params.extend([
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        ])

    # Status filter
    if status:
        count_query += " AND status = %s"
        count_params.append(status)

    cursor.execute(count_query, count_params)

    total_count = cursor.fetchone()[0]

    # -----------------------------------
    # Main query
    # -----------------------------------

    query = """
        SELECT order_id,
               customer_id,
               material_id,
               quantity,
               status,
               order_date
        FROM sales_orders
        WHERE 1=1
    """

    params = []

    # Search
    if search:
        query += """
            AND (
                order_id ILIKE %s
                OR customer_id ILIKE %s
                OR material_id ILIKE %s
                OR status ILIKE %s
                OR order_date::text ILIKE %s
            )
        """

        params.extend([
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        ])

    # Status filter
    if status:
        query += " AND status = %s"
        params.append(status)

    # Sorting
    query += f" ORDER BY {order_column} {order_direction}"

    # Pagination
    query += " LIMIT %s OFFSET %s"

    params.extend([per_page, offset])

    cursor.execute(query, params)

    sales_orders = cursor.fetchall()

    # Calculate total pages
    total_pages = (total_count + per_page - 1) // per_page

    cursor.close()
    connection.close()

    return render_template(
        "sales_orders.html",
        sales_orders=sales_orders,
        search=search,
        status=status,
        sort_by=sort_by,
        sort_order=sort_order,
        page=page,
        total_pages=total_pages
    )

@app.route("/support_requests")
def support_requests():

    search = request.args.get("search", "").strip()
    status = request.args.get("status", "").strip()

    sort_by = request.args.get("sort_by", "request_id")
    sort_order = request.args.get("sort_order", "asc")

    # Pagination
    page = request.args.get("page", 1, type=int)
    per_page = 10

    # Allowed columns for sorting
    sort_options = {
        "request_id": "request_id",
        "issue_type": "issue_type",
        "description": "description",
        "status": "status",
        "created_date": "created_date"
    }

    # Prevent invalid column names
    order_column = sort_options.get(sort_by, "request_id")

    # Only allow ASC / DESC
    order_direction = "DESC" if sort_order == "desc" else "ASC"

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT request_id,
               issue_type,
               description,
               status,
               created_date
        FROM support_requests
        WHERE 1=1
    """

    count_query = """
        SELECT COUNT(*)
        FROM support_requests
        WHERE 1=1
    """

    params = []
    count_params = []

    # Search
    if search:

        search_condition = """
            AND (
                request_id ILIKE %s
                OR issue_type ILIKE %s
                OR description ILIKE %s
                OR status ILIKE %s
                OR created_date::text ILIKE %s
            )
        """

        query += search_condition
        count_query += search_condition

        search_params = [
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        ]

        params.extend(search_params)
        count_params.extend(search_params)

    # Status filter
    if status:
        query += " AND status = %s"
        count_query += " AND status = %s"

        params.append(status)
        count_params.append(status)

    # Get total number of records
    cursor.execute(count_query, count_params)
    total_records = cursor.fetchone()[0]

    # Calculate total pages
    total_pages = (total_records + per_page - 1) // per_page

    # Prevent invalid page numbers
    if page < 1:
        page = 1

    if total_pages > 0 and page > total_pages:
        page = total_pages

    # Pagination offset
    offset = (page - 1) * per_page

    # Sorting + Pagination
    query += f"""
        ORDER BY {order_column} {order_direction}
        LIMIT %s OFFSET %s
    """

    params.extend([per_page, offset])

    cursor.execute(query, params)

    support_requests = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "support_requests.html",
        support_requests=support_requests,
        search=search,
        status=status,
        sort_by=sort_by,
        sort_order=sort_order,
        page=page,
        per_page=per_page,
        total_records=total_records,
        total_pages=total_pages
    )

if __name__ == "__main__":
    app.run(debug=True)