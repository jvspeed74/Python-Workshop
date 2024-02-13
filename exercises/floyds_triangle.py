"""
Name: Jalen Vaughn
Date: 2/13/24
File: floyd's_triangle.py
Description: Script that prints out a Floyd's triangle with a given number of rows
Dependencies/Imports: None
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


def floyd_triangle(rows: int) -> None:
    """
    1
    0 1
    1 0 1
    0 1 0 1
    1 0 1 0 1

    Notes:
    - rows is an array of 0's and 1's.
    - if rows[i] is even, the start of the row is 1
    - if rows[i] is odd, the start of the row is 0
    - Length of row is len(rows[i]) + 1
    - 1 is always the last num to appear in a row
    - start with 1,
    :param rows: The amount of rows for the function to print.
    :type rows: int
    :return: Floyd's Triangle representing the given parameter
    :rtype: None
    """
    for i in range(rows):
        output = ""
        for j in range(i + 1):
            # base case
            if j == i:
                output += "1"
                print(output)
                break

            # print 1 if row and column index is equal
            if i % 2 == 0 and j % 2 == 0:
                output += "1" + " "

            # print 1 if the sum of row and column index is even
            elif (i + j) % 2 == 0:
                output += "1" + " "

            else:
                output += "0" + " "


def main():
    floyd_triangle(get_input())


main()
