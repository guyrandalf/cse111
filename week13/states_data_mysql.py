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

def main():
    try:
        states = get_states

        for row in states():
            # Print the results
            print(f'State: {row[1].upper()} ')
            print(f'Local Govt Areas: {row[2]} ')

    except:
        print('Connection not established')

def get_states():
    """ Queries the database and gets list of all states from the 'states' table """
    
    mycursor.execute(
            "SELECT * FROM states")   
    get_all_states = mycursor.fetchall()
    return get_all_states

if __name__ == "__main__":
    main()
