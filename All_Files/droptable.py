import cx_Oracle

# Oracle Database configuration
oracle_username = "system"
oracle_password = "shubrat"
oracle_dsn = "ORCL"  # Replace with your database DSN if necessary

# Step 2: Drop the existing students table (if exists)
def drop_table():
    try:
        # Establish a connection to the Oracle database
        connection = cx_Oracle.connect(oracle_username, oracle_password, oracle_dsn)
        cursor = connection.cursor()

        # SQL command to drop the table
        drop_sql = "DROP TABLE SYSTEM.STUDENTS CASCADE CONSTRAINTS"
        
        # Execute the drop table command
        cursor.execute(drop_sql)
        print("Table dropped successfully.")
        
        # Commit and close the connection
        connection.commit()
        cursor.close()
        connection.close()
        
    except cx_Oracle.DatabaseError as e:
        print(f"Error dropping table: {e}")

# Test the drop_table function
drop_table()
