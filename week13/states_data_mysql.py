import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cse111"
)

mycursor = mydb.cursor()


def get_states():
    """ Queries the database and gets list of all states and local government areas from the table """
    mycursor.execute(
        "SELECT * FROM states")
    get_all_states = mycursor.fetchall()

    return get_all_states


def get_a_state(id):
    """ Queries the database and gets one state and it's local government areas from the table """
    mycursor.execute(
        f"SELECT * FROM states WHERE id = {id} LIMIT 1"
    )
    get_one_state = mycursor.fetchall()

    return get_one_state


def main():
    try:
        while True:
            # all_states = get_states
            # one_state = get_a_state
            user_input_one = int(
                input('Enter 1 to select all or 2 to select one state: '))

            if user_input_one == 1:
                all_states = get_states
                counter = 0
                for row in all_states():
                    # Print the results
                    counter = counter + 1
                    print(f'({counter}) State: {row[1].upper()} ')
                    print(f'Local Govt Areas: {row[2]} ')
                    print()

            elif user_input_one == 2:
                user_input_two = int(input(
                    'Enter state id: '))
                if user_input_two >= 1 and user_input_two <= 37:                
                    for row in get_a_state(user_input_two):
                        # Print the results
                        print(f'State: {row[1].upper()} ')
                        print(f'Local Govt Areas: {row[2]} ')                    
                else:
                    print('You entered a wrong option')
            else:
                print('You entered a wrong option')

    finally:
        mydb.close()


if __name__ == "__main__":
    main()
