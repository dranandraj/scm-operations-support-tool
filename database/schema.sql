CREATE TABLE customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    customer_name VARCHAR(100),
    country VARCHAR(50),
    status VARCHAR(20)
);

CREATE TABLE materials (
    material_id VARCHAR(10) PRIMARY KEY,
    material_name VARCHAR(100),
    category VARCHAR(50),
    plant VARCHAR(20),
    price INTEGER,
    status VARCHAR(20)
);

CREATE TABLE sales_orders (
    order_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10),
    material_id VARCHAR(10),
    quantity INTEGER,
    status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (material_id) REFERENCES materials(material_id)
);

CREATE TABLE support_requests (
    request_id VARCHAR(10) PRIMARY KEY,
    issue_type VARCHAR(100),
    description TEXT,
    status VARCHAR(20),
    created_date DATE
);