


import csv
import MySQLdb

# Open the CSV file
with open("index.csv", 'r') as file:
    reader = csv.reader(file)
    
    # Skip the header row if your CSV has headers
    next(reader, None)
    
    # Establish a connection to the MySQL database
    connection = MySQLdb.connect(
        user='root',
        passwd='9900',  # MySQLdb uses 'passwd' instead of 'password'
        host='localhost',
        port=3306,  # Port must be an integer
        db='indexcsv'  # Use 'db' instead of 'database'
    )
    
    cursor = connection.cursor()
    
    # Iterate through rows and insert data into the MySQL table
    for row in reader:
        try:
            cursor.execute(
                'INSERT INTO transactions (date, datetime, cash_type, card, money, coffee_name) '
                'VALUES (%s, %s, %s, %s, %s, %s)', 
                row
            )
        except Exception as e:
            print(f"Error occurred: {e} for row {row}")
    
    # Commit the changes to the database
    connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

print("CSV data uploaded successfully!")
