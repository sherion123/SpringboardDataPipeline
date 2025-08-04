import mysql.connector
import csv
import configparser
import datetime
import os

# Set work directory to script location
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join (base_dir, "third_party_sales.csv")

# Connect to MySQL database
def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(user='<username>'
                                            ,password='<password>'
                                            ,host='<hostname>'
                                            ,port='3306'
                                            ,database='<database_name>')
    except Exception as error:
        print("Error while connecting to database for job tracker", error)
    return connection

# Function to create 'sales' table DDL
def create_sales_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            ticket_id INT
           ,trans_date DATE
           ,event_id INT
           ,event_name VARCHAR(50)
           ,event_date DATE
           ,event_type VARCHAR(10)
           ,event_city VARCHAR(20)
           ,customer_id INT
           ,price DECIMAL
           ,num_tickets INT
           );
    """)
    connection.commit()
    cursor.close()

# Function to load CSV data
def load_third_party(connection, file_path_csv):
    cursor = connection.cursor()

    with open(file_path_csv, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            cursor.execute("""
                INSERT INTO sales (ticket_id
                                  ,trans_date
                                  ,event_id
                                  ,event_name
                                  ,event_date
                                  ,event_type
                                  ,event_city
                                  ,customer_id
                                  ,price
                                  ,num_tickets)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, row)
    connection.commit()
    cursor.close()
    return

# Function to display statistical information: Recommend popular events by finding the top-selling tickets for the past month.
def query_popular_tickets(connection):
    # Get the 3 most popular ticket within the database
    sql_statement = """
                    SELECT event_name
                          ,SUM(num_tickets) as total_sold
                    FROM sales
                    GROUP BY event_name
                    ORDER BY total_sold DESC
                    LIMIT 3;"""
    cursor = connection.cursor()
    cursor.execute(sql_statement)
    records = cursor.fetchall()
    cursor.close()
    return records

# Function to print the 3 most popular ticket
def print_popular_tickets(records):
    print("\nHere are the 3 most popular tickets:\n")
    for event_name, total in records:
        print(f"- {event_name} ({total} tickets sold)")

# Main function to run the script
if __name__ == "__main__":
    conn = get_db_connection()
    if conn:
        create_sales_table(conn)
        load_third_party(conn, file_path)
        popular_tickets = query_popular_tickets(conn)
        print_popular_tickets(popular_tickets)
        conn.close()



