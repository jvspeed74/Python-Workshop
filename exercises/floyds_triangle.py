"""
Name: Jalen Vaughn
Date: 2/13/24
File: floyd's_triangle.py
Description: Script that prints out a Floyd's triangle with a given number of rows
Dependencies/Imports: 
"""


def get_input() -> int:
    """
    Gets user input and type casts it to int.
    :return: A positive integer
    :rtype: int
    """
    while True:
        user_input = input("Enter an integer: ")

        try:
            user_input = int(user_input)

        except ValueError:
            print("Invalid number")
            continue

        if user_input <= 0:
            print("Please enter a positive integer.")
            continue

        return user_input


def floyd_triangle(rows):
    """

    :param rows:
    :type rows:
    :return:
    :rtype:
    """
    for i in range(rows):  # row
        this_row = ''
        for j in range(i + 1):  # column
            if j != 0:
                this_row += " "

            if i % 2 == j % 2:
                this_row += "1"
            else:
                this_row += "0"
        print(this_row)


