import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="cse111"
)

# Check if connection succeeds
if mydb:
    # Create a cursor object
    mycursor = mydb.cursor()

    # Execute a query
    mycursor.execute("SELECT * FROM users")

    # Retrieve the results
    results = mycursor.fetchall()
else:
  print('Connection not established')

# Print the results
for row in results:
  print(row)
