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
        all_states = get_states
        # one_state = get_a_state
        counter = 0
        for row in all_states():
            # Print the results
            counter = counter + 1
            print(f'({counter}) State: {row[1].upper()} ')
            print(f'Local Govt Areas: {row[2]} ')
            print()

        # for row in one_state():
        #     # Print the results
        #     print(f'State: {row[1].upper()} ')
        #     print(f'Local Govt Areas: {row[2]} ')
        #     print()

    except:
        print('Connection not established')

    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()


def get_states():
    """ Queries the database and gets list of all states and local government areas from the table """
    mycursor.execute(
        "SELECT * FROM states")
    get_all_states = mycursor.fetchall()

    return get_all_states


if __name__ == "__main__":
    main()
