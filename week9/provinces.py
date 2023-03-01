from typing import List

def main():
    list = read_list("provinces.txt")
    print(list)
    list.pop(0)
    list.pop()

    for i in range(len(list)):
        if list[i] == "AB":
            list[i] = "Alberta"
    #print(list)

    # call the list.count method which will count the number
    # of times that ablberta appears in the list
    count = list.count("Alberta")

    print()
    print(f"Alberta occurs {count} times in the modified list")


def read_list(filename):
    """Read the contents of a text file into a list
    and return the list that contains the lines of text
    
    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list that will store
    # the lines of a text from the text file
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and the end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list
            text_list.append(clean_line)
    
    # Return the list that contains the lines of text
    return text_list        

# If this file was executed like this:
# > python provinces.py
# then call the main function. However, if the file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()