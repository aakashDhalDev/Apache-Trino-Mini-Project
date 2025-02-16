import mysql.connector
import psycopg2
import pyodbc
import pymysql

def fetch_mysql_data():
    try:
        cnx = pymysql.connect(
            host="localhost",
            port=3307,
            user="root",
            password="secret",
            database="mydb"
        )

        if cnx.open:
            print("Connected to the database")
            with cnx.cursor() as cursor:
                    cursor.execute("SELECT * FROM customers")
                    customers = cursor.fetchall()

                    if customers:
                        print(f"Total records: {len(customers)}")
                        for customer in customers:
                            print(customer)
                    else:
                        print("No records found in the customers table.")
    except pymysql.MySQLError as e:
        print("Error fetching MySQL data:", e)

def fetch_postgresql_data():
    try:
        conn = psycopg2.connect(
            host="localhost",     
            port=5433,
            user="user",
            password="secret",
            database="mydb"
        )
        cursor = conn.cursor()
        print(cursor)
        cursor.execute("SELECT * FROM orders")
        rows = cursor.fetchall()
        print("PostgreSQL - Orders Table:")
        print(f"Fetched {len(rows)} rows.")
        for row in rows:
            print(row)
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error fetching PostgreSQL data:", e)

def fetch_sqlserver_data():
    try:
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
        print(cursor)
        cursor.execute("SELECT * FROM payments")
        rows = cursor.fetchall()
        print("SQL Server - Payments Table:")
        print(f"Fetched {len(rows)} rows.")
        for row in rows:
            print(row)
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error fetching SQL Server data:", e)

if __name__ == '__main__':
    fetch_mysql_data()
    print("\n" + "="*50 + "\n")
    fetch_postgresql_data()
    print("\n" + "="*50 + "\n")
    fetch_sqlserver_data()
