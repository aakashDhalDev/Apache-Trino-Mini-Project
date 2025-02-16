import trino

# Establish a connection to the Trino server
conn = trino.dbapi.connect(
    host='localhost',       # Trino's host; adjust if necessary
    port=8081,              # Trino's port (published port from Docker)
    user='trino',           # Provide a user name (can be any string if not using authentication)
    catalog='mysql',        # Default catalog; fully qualified table names override this
    schema='default'        # Default schema for the chosen catalog
)

cursor = conn.cursor()

# Define a federated query joining tables across different catalogs
query = """
            SELECT 
                c.name, 
                o.order_date, 
                p.payment_date, 
                p.amount AS payment_amount
            FROM mysql.mydb.customers AS c
            JOIN postgresql.public.orders AS o 
                ON c.id = o.customer_id
            JOIN mssql.dbo.payments AS p 
                ON o.order_id = p.order_id
        """
query_new = """
                select * from mysql.mydb.customers
            """
# Execute the query and fetch the results
cursor.execute(query_new)
rows = cursor.fetchall()

# Print the federated query results
print("Federated query results:")
for row in rows:
    print(row)

# Clean up by closing the cursor and connection
cursor.close()
conn.close()
