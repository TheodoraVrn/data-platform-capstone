# Import libraries required for connecting to mysql

# Import libraries required for connecting to DB2 or PostgreSql
import psycopg2
import mysql.connector

# Connect to MySQL
mysql_conn = mysql.connector.connect(
    user='root', 
    password='',
    host='',
    database='sales'
    )

# Connect to DB2 or PostgreSql
pg_conn = psycopg2.connect(
    host="",
    database="sales",  # or whichever database name is specified in your lab instructions
    user="postgres",
    password=""
)

# Find out the last rowid from DB2 data warehouse or PostgreSql data warehouse
# The function get_last_rowid must return the last rowid of the table sales_data on the IBM DB2 database or PostgreSql.

def get_last_rowid():
    cursor = pg_conn.cursor()
    cursor.execute("SELECT MAX(rowid) FROM sales_data;")
    result = cursor.fetchone()[0]
    cursor.close()
    return result if result is not None else 0


last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)

# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.

def get_latest_records(rowid):
    cursor = mysql_conn.cursor()
    query = "SELECT * FROM sales_data WHERE rowid > %s;"
    cursor.execute(query, (rowid,))
    records = cursor.fetchall()
    cursor.close()
    return records	

new_records = get_latest_records(last_row_id)

print("New rows on staging datawarehouse = ", len(new_records))

# Insert the additional records from MySQL into DB2 or PostgreSql data warehouse.
# The function insert_records must insert all the records passed to it into the sales_data table in IBM DB2 database or PostgreSql.

def insert_records(records):
    if not records:
        return
    list_ofrecords = records
    cursor = pg_conn.cursor()

    for row in list_ofrecords:
  
        SQL= """
        INSERT INTO sales_data (rowid, product_id, customer_id, price, quantity, timestamp)
        VALUES (%s, %s, %s, 0, %s, NULL);
    """
        cursor.execute(SQL,row);
        pg_conn.commit()

    cursor.close()

insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse
mysql_conn.close()

# disconnect from DB2 or PostgreSql data warehouse 
pg_conn.close()

# End of program
