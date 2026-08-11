import io
import csv
import openpyxl
from openpyxl import Workbook
from flask import Flask, make_response, render_template, request, send_file, redirect, url_for, Response
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
    per_page = request.args.get("per_page", 10, type=int)

    # Allowed page sizes
    allowed_page_sizes = [10, 25, 50, 100]

    if per_page not in allowed_page_sizes:
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

    # Prevent invalid column names
    order_column = sort_options.get(sort_by, "customer_id")

    # Only allow ASC / DESC
    order_direction = "DESC" if sort_order == "desc" else "ASC"

    connection = get_connection()
    cursor = connection.cursor()

    # Main query
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

    # Search for count
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

    # Country filter for count
    if country:
        count_query += " AND country = %s"
        count_params.append(country)

    # Status filter for count
    if status:
        count_query += " AND status = %s"
        count_params.append(status)

    cursor.execute(count_query, count_params)

    total_records = cursor.fetchone()[0]

    # Calculate total pages
    total_pages = max(
        1,
        (total_records + per_page - 1) // per_page
    )

    # Prevent invalid page number
    if page > total_pages:
        page = total_pages

    # Calculate offset
    offset = (page - 1) * per_page

    # Sorting + Pagination
    query += f"""
        ORDER BY {order_column} {order_direction}
        LIMIT %s OFFSET %s
    """

    params.extend([
        per_page,
        offset
    ])

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
        total_pages=total_pages,
        current_endpoint="customers"
    )

@app.route("/customers/export/csv")
def export_customers_csv():

    search = request.args.get("search", "").strip()
    country = request.args.get("country", "").strip()
    status = request.args.get("status", "").strip()

    sort_by = request.args.get("sort_by", "customer_id")
    sort_order = request.args.get("sort_order", "asc")

    # Allowed sorting columns
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

    # Sorting
    query += f" ORDER BY {order_column} {order_direction}"

    cursor.execute(query, params)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow([
        "Customer ID",
        "Customer Name",
        "Country",
        "Status"
    ])

    writer.writerows(rows)

    response = make_response(output.getvalue())

    response.headers["Content-Disposition"] = (
        "attachment; filename=customers.csv"
    )

    response.headers["Content-Type"] = "text/csv"

    return response

@app.route("/customers/export/excel")
def export_customers_excel():

    search = request.args.get("search", "").strip()
    country = request.args.get("country", "").strip()
    status = request.args.get("status", "").strip()

    sort_by = request.args.get("sort_by", "customer_id")
    sort_order = request.args.get("sort_order", "asc")

    # Allowed sorting columns
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

    # Sorting
    query += f" ORDER BY {order_column} {order_direction}"

    cursor.execute(query, params)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    # Create Excel workbook
    workbook = openpyxl.Workbook()
    worksheet = workbook.active
    worksheet.title = "Customers"

    # Header
    worksheet.append([
        "Customer ID",
        "Customer Name",
        "Country",
        "Status"
    ])

    # Data
    for row in rows:
        worksheet.append(row)

    # Auto-size columns
    for column in worksheet.columns:
        max_length = 0
        column_letter = column[0].column_letter

        for cell in column:
            if cell.value is not None:
                max_length = max(
                    max_length,
                    len(str(cell.value))
                )

        worksheet.column_dimensions[column_letter].width = max_length + 2

    # Save workbook to memory
    output = io.BytesIO()
    workbook.save(output)
    output.seek(0)

    return send_file(
        output,
        as_attachment=True,
        download_name="customers.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
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

    # Rows per page
    per_page = request.args.get("per_page", 10, type=int)

    # Allow only valid page sizes
    if per_page not in [10, 25, 50, 100]:
        per_page = 10

    if page < 1:
        page = 1

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

    total_records = cursor.fetchone()[0]

    # -----------------------------------
    # Calculate total pages
    # -----------------------------------

    total_pages = max(
        1,
        (total_records + per_page - 1) // per_page
    )

    # Prevent invalid page number
    if page > total_pages:
        page = total_pages

    offset = (page - 1) * per_page

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

    # Sorting + Pagination
    query += f"""
        ORDER BY {order_column} {order_direction}
        LIMIT %s OFFSET %s
    """

    params.extend([
        per_page,
        offset
    ])

    cursor.execute(query, params)

    materials = cursor.fetchall()

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
        per_page=per_page,
        total_records=total_records,
        total_pages=total_pages
    )

@app.route("/materials/export/csv")
def export_materials_csv():

    search = request.args.get("search", "").strip()
    category = request.args.get("category", "").strip()
    plant = request.args.get("plant", "").strip()
    status = request.args.get("status", "").strip()

    sort_by = request.args.get("sort_by", "material_id")
    sort_order = request.args.get("sort_order", "asc")

    sort_options = {
        "material_id": "material_id",
        "material_name": "CAST(REGEXP_REPLACE(material_name, '[^0-9]', '', 'g') AS INTEGER)",
        "category": "category",
        "plant": "plant",
        "price": "price",
        "status": "status"
    }

    order_column = sort_options.get(sort_by, "material_id")
    order_direction = "DESC" if sort_order == "desc" else "ASC"

    connection = get_connection()
    cursor = connection.cursor()

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

    if category:
        query += " AND category = %s"
        params.append(category)

    if plant:
        query += " AND plant = %s"
        params.append(plant)

    if status:
        query += " AND status = %s"
        params.append(status)

    query += f" ORDER BY {order_column} {order_direction}"

    cursor.execute(query, params)

    materials = cursor.fetchall()

    cursor.close()
    connection.close()

    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow([
        "Material ID",
        "Material Name",
        "Category",
        "Plant",
        "Price",
        "Status"
    ])

    writer.writerows(materials)

    output.seek(0)

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=materials.csv"
        }
    )

@app.route("/materials/export/excel")
def export_materials_excel():

    search = request.args.get("search", "").strip()
    category = request.args.get("category", "").strip()
    plant = request.args.get("plant", "").strip()
    status = request.args.get("status", "").strip()

    sort_by = request.args.get("sort_by", "material_id")
    sort_order = request.args.get("sort_order", "asc")

    # -----------------------------------
    # Allowed columns for sorting
    # -----------------------------------

    sort_options = {
        "material_id": "material_id",
        "material_name": "material_name",
        "category": "category",
        "plant": "plant",
        "price": "price",
        "status": "status"
    }

    # Prevent invalid column names
    order_column = sort_options.get(sort_by, "material_id")

    # Only allow ASC / DESC
    order_direction = "DESC" if sort_order == "desc" else "ASC"

    # -----------------------------------
    # Database connection
    # -----------------------------------

    connection = get_connection()
    cursor = connection.cursor()

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

    # -----------------------------------
    # Search
    # -----------------------------------

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

    # -----------------------------------
    # Category filter
    # -----------------------------------

    if category:
        query += " AND category = %s"
        params.append(category)

    # -----------------------------------
    # Plant filter
    # -----------------------------------

    if plant:
        query += " AND plant = %s"
        params.append(plant)

    # -----------------------------------
    # Status filter
    # -----------------------------------

    if status:
        query += " AND status = %s"
        params.append(status)

    # -----------------------------------
    # Sorting
    # -----------------------------------

    query += f" ORDER BY {order_column} {order_direction}"

    cursor.execute(query, params)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    # -----------------------------------
    # Create Excel workbook
    # -----------------------------------

    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Materials"

    # Header
    worksheet.append([
        "Material ID",
        "Material Name",
        "Category",
        "Plant",
        "Price",
        "Status"
    ])

    # Data
    for row in rows:
        worksheet.append(row)

    # -----------------------------------
    # Auto width columns
    # -----------------------------------

    for column in worksheet.columns:

        max_length = 0
        column_letter = column[0].column_letter

        for cell in column:
            if cell.value is not None:
                max_length = max(
                    max_length,
                    len(str(cell.value))
                )

        worksheet.column_dimensions[column_letter].width = max_length + 2

    # -----------------------------------
    # Save workbook to memory
    # -----------------------------------

    output = io.BytesIO()

    workbook.save(output)

    output.seek(0)

    # -----------------------------------
    # Download Excel file
    # -----------------------------------

    return send_file(
        output,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        as_attachment=True,
        download_name="materials.xlsx"
    )

@app.route("/sales_orders")
def sales_orders():

    search = request.args.get("search", "").strip()
    status = request.args.get("status", "").strip()

    sort_by = request.args.get("sort_by", "order_id")
    sort_order = request.args.get("sort_order", "asc")

    # -----------------------------------
    # Pagination
    # -----------------------------------

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    # Allowed page sizes
    allowed_per_page = [10, 25, 50, 100]

    if per_page not in allowed_per_page:
        per_page = 10

    if page < 1:
        page = 1

    # -----------------------------------
    # Allowed columns for sorting
    # -----------------------------------

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
    # Calculate total pages
    # -----------------------------------

    total_pages = max(
        1,
        (total_count + per_page - 1) // per_page
    )

    # Prevent invalid page number
    if page > total_pages:
        page = total_pages

    # Calculate offset
    offset = (page - 1) * per_page

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

    # -----------------------------------
    # Sorting
    # -----------------------------------

    query += f"""
        ORDER BY {order_column} {order_direction}
    """

    # -----------------------------------
    # Pagination
    # -----------------------------------

    query += """
        LIMIT %s OFFSET %s
    """

    params.extend([
        per_page,
        offset
    ])

    cursor.execute(query, params)

    sales_orders = cursor.fetchall()

    cursor.close()
    connection.close()

    # -----------------------------------
    # Render template
    # -----------------------------------

    return render_template(
        "sales_orders.html",
        sales_orders=sales_orders,
        search=search,
        status=status,
        sort_by=sort_by,
        sort_order=sort_order,
        page=page,
        per_page=per_page,
        total_count=total_count,
        total_pages=total_pages
    )

@app.route("/sales_orders/export/csv")
def export_sales_orders_csv():

    search = request.args.get("search", "").strip()
    status = request.args.get("status", "").strip()

    sort_by = request.args.get("sort_by", "order_id")
    sort_order = request.args.get("sort_order", "asc")

    # -----------------------------------
    # Allowed columns for sorting
    # -----------------------------------

    sort_options = {
        "order_id": "order_id",
        "customer_id": "customer_id",
        "material_id": "material_id",
        "quantity": "quantity",
        "status": "status",
        "order_date": "order_date"
    }

    order_column = sort_options.get(sort_by, "order_id")

    order_direction = "DESC" if sort_order == "desc" else "ASC"

    # -----------------------------------
    # Database connection
    # -----------------------------------

    connection = get_connection()
    cursor = connection.cursor()

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

    # -----------------------------------
    # Search
    # -----------------------------------

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

    # -----------------------------------
    # Status filter
    # -----------------------------------

    if status:
        query += " AND status = %s"
        params.append(status)

    # -----------------------------------
    # Sorting
    # -----------------------------------

    query += f" ORDER BY {order_column} {order_direction}"

    cursor.execute(query, params)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    # -----------------------------------
    # Create CSV
    # -----------------------------------

    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow([
        "Sales Order ID",
        "Customer ID",
        "Material ID",
        "Quantity",
        "Status",
        "Order Date"
    ])

    for row in rows:
        writer.writerow(row)

    # -----------------------------------
    # Return CSV
    # -----------------------------------

    response = Response(
        output.getvalue(),
        mimetype="text/csv"
    )

    response.headers["Content-Disposition"] = (
        "attachment; filename=sales_orders.csv"
    )

    return response

@app.route("/sales_orders/export/excel")
def export_sales_orders_excel():

    search = request.args.get("search", "").strip()
    status = request.args.get("status", "").strip()

    sort_by = request.args.get("sort_by", "order_id")
    sort_order = request.args.get("sort_order", "asc")

    # -----------------------------------
    # Allowed columns for sorting
    # -----------------------------------

    sort_options = {
        "order_id": "order_id",
        "customer_id": "customer_id",
        "material_id": "material_id",
        "quantity": "quantity",
        "status": "status",
        "order_date": "order_date"
    }

    order_column = sort_options.get(sort_by, "order_id")

    order_direction = "DESC" if sort_order == "desc" else "ASC"

    # -----------------------------------
    # Database connection
    # -----------------------------------

    connection = get_connection()
    cursor = connection.cursor()

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

    # -----------------------------------
    # Search
    # -----------------------------------

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

    # -----------------------------------
    # Status filter
    # -----------------------------------

    if status:
        query += " AND status = %s"
        params.append(status)

    # -----------------------------------
    # Sorting
    # -----------------------------------

    query += f" ORDER BY {order_column} {order_direction}"

    cursor.execute(query, params)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    # -----------------------------------
    # Create Excel workbook
    # -----------------------------------

    workbook = Workbook()

    worksheet = workbook.active
    worksheet.title = "Sales Orders"

    # Header
    worksheet.append([
        "Sales Order ID",
        "Customer ID",
        "Material ID",
        "Quantity",
        "Status",
        "Order Date"
    ])

    # Data
    for row in rows:
        worksheet.append(row)

    # -----------------------------------
    # Auto width columns
    # -----------------------------------

    for column in worksheet.columns:

        max_length = 0
        column_letter = column[0].column_letter

        for cell in column:

            if cell.value is not None:
                max_length = max(
                    max_length,
                    len(str(cell.value))
                )

        worksheet.column_dimensions[column_letter].width = max_length + 2

    # -----------------------------------
    # Save Excel to memory
    # -----------------------------------

    output = io.BytesIO()

    workbook.save(output)

    output.seek(0)

    # -----------------------------------
    # Download Excel
    # -----------------------------------

    return send_file(
        output,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        as_attachment=True,
        download_name="sales_orders.xlsx"
    )

@app.route("/support_requests")
def support_requests():

    search = request.args.get("search", "").strip()
    status = request.args.get("status", "").strip()

    sort_by = request.args.get("sort_by", "request_id")
    sort_order = request.args.get("sort_order", "asc")

    # Pagination
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    # Allowed rows per page
    allowed_per_page = [10, 25, 50, 100]

    if per_page not in allowed_per_page:
        per_page = 10

    if page < 1:
        page = 1

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

    # -----------------------------------
    # Main Query
    # -----------------------------------

    query = """
        SELECT request_id,
               issue_type,
               description,
               status,
               created_date
        FROM support_requests
        WHERE 1=1
    """

    # -----------------------------------
    # Count Query
    # -----------------------------------

    count_query = """
        SELECT COUNT(*)
        FROM support_requests
        WHERE 1=1
    """

    params = []
    count_params = []

    # -----------------------------------
    # Search
    # -----------------------------------

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

    # -----------------------------------
    # Status Filter
    # -----------------------------------

    if status:

        query += " AND status = %s"
        count_query += " AND status = %s"

        params.append(status)
        count_params.append(status)

    # -----------------------------------
    # Total Records
    # -----------------------------------

    cursor.execute(count_query, count_params)

    total_records = cursor.fetchone()[0]

    # -----------------------------------
    # Total Pages
    # -----------------------------------

    total_pages = max(
        1,
        (total_records + per_page - 1) // per_page
    )

    # Prevent invalid page number
    if page > total_pages:
        page = total_pages

    # -----------------------------------
    # Pagination Offset
    # -----------------------------------

    offset = (page - 1) * per_page

    # -----------------------------------
    # Sorting + Pagination
    # -----------------------------------

    query += f"""
        ORDER BY {order_column} {order_direction}
        LIMIT %s OFFSET %s
    """

    params.extend([
        per_page,
        offset
    ])

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

@app.route("/support_requests/export/csv")
def export_support_requests_csv():

    search = request.args.get("search", "").strip()
    status = request.args.get("status", "").strip()

    sort_by = request.args.get("sort_by", "request_id")
    sort_order = request.args.get("sort_order", "asc")

    # -----------------------------------
    # Allowed columns for sorting
    # -----------------------------------

    sort_options = {
        "request_id": "request_id",
        "issue_type": "issue_type",
        "description": "description",
        "status": "status",
        "created_date": "created_date"
    }

    order_column = sort_options.get(sort_by, "request_id")

    order_direction = "DESC" if sort_order == "desc" else "ASC"

    # -----------------------------------
    # Database connection
    # -----------------------------------

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

    params = []

    # -----------------------------------
    # Search
    # -----------------------------------

    if search:
        query += """
            AND (
                request_id ILIKE %s
                OR issue_type ILIKE %s
                OR description ILIKE %s
                OR status ILIKE %s
                OR created_date::text ILIKE %s
            )
        """

        params.extend([
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        ])

    # -----------------------------------
    # Status filter
    # -----------------------------------

    if status:
        query += " AND status = %s"
        params.append(status)

    # -----------------------------------
    # Sorting
    # -----------------------------------

    query += f" ORDER BY {order_column} {order_direction}"

    cursor.execute(query, params)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    # -----------------------------------
    # Create CSV
    # -----------------------------------

    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow([
        "Request ID",
        "Issue Type",
        "Description",
        "Status",
        "Created Date"
    ])

    for row in rows:
        writer.writerow(row)

    # -----------------------------------
    # Return CSV
    # -----------------------------------

    response = Response(
        output.getvalue(),
        mimetype="text/csv"
    )

    response.headers["Content-Disposition"] = (
        "attachment; filename=support_requests.csv"
    )

    return response

@app.route("/support_requests/export/excel")
def export_support_requests_excel():

    search = request.args.get("search", "").strip()
    status = request.args.get("status", "").strip()

    sort_by = request.args.get("sort_by", "request_id")
    sort_order = request.args.get("sort_order", "asc")

    # -----------------------------------
    # Allowed columns for sorting
    # -----------------------------------

    sort_options = {
        "request_id": "request_id",
        "issue_type": "issue_type",
        "description": "description",
        "status": "status",
        "created_date": "created_date"
    }

    order_column = sort_options.get(sort_by, "request_id")

    order_direction = "DESC" if sort_order == "desc" else "ASC"

    # -----------------------------------
    # Database connection
    # -----------------------------------

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

    params = []

    # -----------------------------------
    # Search
    # -----------------------------------

    if search:
        query += """
            AND (
                request_id ILIKE %s
                OR issue_type ILIKE %s
                OR description ILIKE %s
                OR status ILIKE %s
                OR created_date::text ILIKE %s
            )
        """

        params.extend([
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        ])

    # -----------------------------------
    # Status filter
    # -----------------------------------

    if status:
        query += " AND status = %s"
        params.append(status)

    # -----------------------------------
    # Sorting
    # -----------------------------------

    query += f" ORDER BY {order_column} {order_direction}"

    cursor.execute(query, params)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    # -----------------------------------
    # Create Excel workbook
    # -----------------------------------

    workbook = Workbook()

    worksheet = workbook.active
    worksheet.title = "Support Requests"

    # Header
    worksheet.append([
        "Request ID",
        "Issue Type",
        "Description",
        "Status",
        "Created Date"
    ])

    # Data
    for row in rows:
        worksheet.append(row)

    # -----------------------------------
    # Auto width columns
    # -----------------------------------

    for column in worksheet.columns:

        max_length = 0
        column_letter = column[0].column_letter

        for cell in column:

            if cell.value is not None:
                max_length = max(
                    max_length,
                    len(str(cell.value))
                )

        worksheet.column_dimensions[column_letter].width = max_length + 2

    # -----------------------------------
    # Save Excel to memory
    # -----------------------------------

    output = io.BytesIO()

    workbook.save(output)

    output.seek(0)

    # -----------------------------------
    # Download Excel
    # -----------------------------------

    return send_file(
        output,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        as_attachment=True,
        download_name="support_requests.xlsx"
    )

if __name__ == "__main__":
    app.run(debug=True)