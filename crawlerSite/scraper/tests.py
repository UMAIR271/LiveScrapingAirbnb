import mysql.connector

# Replace these placeholders with your RDS instance details
db_host = '34.23.87.242'
db_port = '3306'
db_name = 'cleanster-logs'
db_user = 'airbnb_root'
db_password = '7BQ+NLokL<L,x@+r'

try:
    print("Connecting to")
    conn = mysql.connector.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port,
        database=db_name
    )
    print(conn)
    if conn.is_connected():
        print("Connected to the database!")

        # Now you can execute SQL queries using this connection
        # ...

except mysql.connector.Error as e:
    print("Error connecting to the database:", e)
finally:
    if conn.is_connected():
        conn.close()
        print("Connection closed.")
