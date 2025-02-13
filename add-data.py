import mysql.connector
import psycopg2
import pyodbc

def populate_mysql():
    print("Populating MySQL (customers table)...")
    # Connect to MySQL (adjust host if needed, e.g., "mysql-server" if running in Docker network)
    cnx = mysql.connector.connect(
        host="localhost",
        user="user",
        password="secret",
        database="mydb"
    )
    cursor = cnx.cursor()

    # Create the customers table
    create_table = """
        CREATE TABLE IF NOT EXISTS customers (
            id INT PRIMARY KEY,
            name VARCHAR(50),
            email VARCHAR(50),
            city VARCHAR(50),
            country VARCHAR(50)
        )
    """
    cursor.execute(create_table)

    # Clear table if it already exists (optional)
    cursor.execute("DELETE FROM customers")

    # Insert 10 rows into the customers table
    customers_data = [
        (1, 'Alice', 'alice@example.com', 'New York', 'USA'),
        (2, 'Bob', 'bob@example.com', 'Los Angeles', 'USA'),
        (3, 'Charlie', 'charlie@example.com', 'Chicago', 'USA'),
        (4, 'Diana', 'diana@example.com', 'Houston', 'USA'),
        (5, 'Ethan', 'ethan@example.com', 'Phoenix', 'USA'),
        (6, 'Fiona', 'fiona@example.com', 'Philadelphia', 'USA'),
        (7, 'George', 'george@example.com', 'San Antonio', 'USA'),
        (8, 'Hannah', 'hannah@example.com', 'San Diego', 'USA'),
        (9, 'Ian', 'ian@example.com', 'Dallas', 'USA'),
        (10, 'Jane', 'jane@example.com', 'San Jose', 'USA')
    ]
    insert_query = "INSERT INTO customers (id, name, email, city, country) VALUES (%s, %s, %s, %s, %s)"
    cursor.executemany(insert_query, customers_data)
    cnx.commit()
    cursor.close()
    cnx.close()
    print("MySQL table populated.\n")

def populate_postgresql():
    print("Populating PostgreSQL (orders table)...")
    # Connect to PostgreSQL (adjust host if needed, e.g., "postgres-server")
    conn = psycopg2.connect(
        host="localhost",
        port=5433,
        user="user",
        password="secret",
        database="mydb"
    )
    cursor = conn.cursor()

    # Create the orders table
    create_table = """
        CREATE TABLE IF NOT EXISTS orders (
            order_id INT PRIMARY KEY,
            customer_id INT,
            order_date DATE,
            amount DECIMAL(10,2),
            status VARCHAR(20)
        )
    """
    cursor.execute(create_table)

    # Clear table if it exists
    cursor.execute("DELETE FROM orders")

    # Insert 10 rows into the orders table
    orders_data = [
        (1, 1, '2025-01-01', 100.00, 'completed'),
        (2, 2, '2025-01-02', 150.00, 'completed'),
        (3, 3, '2025-01-03', 200.00, 'pending'),
        (4, 4, '2025-01-04', 250.00, 'completed'),
        (5, 5, '2025-01-05', 300.00, 'pending'),
        (6, 6, '2025-01-06', 350.00, 'completed'),
        (7, 7, '2025-01-07', 400.00, 'completed'),
        (8, 8, '2025-01-08', 450.00, 'pending'),
        (9, 9, '2025-01-09', 500.00, 'completed'),
        (10, 10, '2025-01-10', 550.00, 'pending')
    ]
    insert_query = "INSERT INTO orders (order_id, customer_id, order_date, amount, status) VALUES (%s, %s, %s, %s, %s)"
    cursor.executemany(insert_query, orders_data)
    conn.commit()
    cursor.close()
    conn.close()
    print("PostgreSQL table populated.\n")

def populate_sqlserver():
    print("Populating SQL Server (payments table)...")
    # Define connection string for SQL Server (adjust DRIVER, SERVER, and credentials as necessary)
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost,1434;"
        "DATABASE=master;"
        "UID=sa;"
        "PWD=YourStrong!Passw0rd;"
        "TrustServerCertificate=yes;"
    )
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Create the payments table (using IF NOT EXISTS style for SQL Server)
    create_table = """
        IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'payments')
        BEGIN
            CREATE TABLE payments (
                payment_id INT PRIMARY KEY,
                order_id INT,
                payment_date DATE,
                amount DECIMAL(10,2),
                method VARCHAR(20)
            )
        END
    """
    cursor.execute(create_table)
    conn.commit()

    # Clear the table if exists
    cursor.execute("DELETE FROM payments")
    conn.commit()

    # Insert 10 rows into the payments table
    payments_data = [
        (1, 1, '2025-01-02', 100.00, 'credit card'),
        (2, 2, '2025-01-03', 150.00, 'paypal'),
        (3, 3, '2025-01-04', 200.00, 'credit card'),
        (4, 4, '2025-01-05', 250.00, 'debit card'),
        (5, 5, '2025-01-06', 300.00, 'credit card'),
        (6, 6, '2025-01-07', 350.00, 'paypal'),
        (7, 7, '2025-01-08', 400.00, 'credit card'),
        (8, 8, '2025-01-09', 450.00, 'debit card'),
        (9, 9, '2025-01-10', 500.00, 'credit card'),
        (10, 10, '2025-01-11', 550.00, 'paypal')
    ]
    # Use parameter placeholder "?" for pyodbc
    insert_query = "INSERT INTO payments (payment_id, order_id, payment_date, amount, method) VALUES (?, ?, ?, ?, ?)"
    cursor.executemany(insert_query, payments_data)
    conn.commit()
    cursor.close()
    conn.close()
    print("SQL Server table populated.\n")

if __name__ == '__main__':
    # try:
    #     populate_mysql()
    # except Exception as e:
    #     print("Error populating MySQL:", e)
    
    # try:
    #     populate_postgresql()
    # except Exception as e:
    #     print("Error populating PostgreSQL:", e)
    
    try:
        populate_sqlserver()
    except Exception as e:
        print("Error populating SQL Server:", e)
    
    # print("Data population complete. You can now run federated queries from Trino to join these tables.")
