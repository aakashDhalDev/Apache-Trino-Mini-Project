import trino

conn = trino.dbapi.connect(
    host='localhost',      
    port=8081,              
    user='trino',           
    catalog='mysql',        
    schema='default'        
)

cursor = conn.cursor()

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

cursor.execute(query_new)
rows = cursor.fetchall()

print("Federated query results:")
for row in rows:
    print(row)

cursor.close()
conn.close()
