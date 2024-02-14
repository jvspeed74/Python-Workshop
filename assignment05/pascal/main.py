"""
Name: Jalen Vaughn
Date: 2/13/24
File: main.py
Description: Script to build a pascal triangle
Dependencies: None
"""


def get_input() -> int:
    """
    Gets user input and type casts it to int.
    :return: A positive integer
    :rtype: int
    """
    while True:
        # get input
        user_input = input("Enter the number of rows for Pascal's Triangle: ")

        # error handle conversion to integer
        try:
            user_input = int(user_input)

        # catch error
        except ValueError:
            print(f"Invalid input: '{user_input}'. Value must be an integer.")
            continue

        # restart loop if input is negative
        if user_input < 0:
            print("Please enter a positive integer.")
            continue

        # validated integer
        return user_input


def generate_pascal_triangle(n_rows: int) -> list[list[int]]:
    """
    Builds a pascal triangle with the given number of rows. The solution method includes a bottom-up dynamic programming
    approach. Each row is constructed using information from the previous row, and this process continues until the
    desired number of rows is reached.
    :param n_rows: number of rows valued at 1 or more.
    :type n_rows: int
    :return: A pascal triangle built into a two-dimensional list.
    :rtype: list[list[int]]
    """

    # base case: 0 rows should print nothing
    if n_rows == 0:
        return [[]]

    # declare starting point for algorithm
    result: list[list[int]] = [[1]]

    # iterator for rows
    for i in range(n_rows - 1):

        # every row starts with 1
        next_row: list[int] = [1]  # data storage for the next row before being passed to result

        # iterator for data/columns
        for j in range(i + 1):

            # reached the end of the row so break back to outer loop
            if j == i:
                next_row.append(1)  # every row ends with 1
                break

            # walk through the last list in result and add adjacent indexes
            next_row.append(result[-1][j] + result[-1][j + 1])

        # append data/columns to end of list
        result.append(next_row)

    # 2D matrix of Pascal's triangle
    return result


def print_pascal_triangle(blueprint: list[list[int]]) -> None:
    """
    Prints a pyramid shaped pascal triangle to the console.
    :param blueprint: A pascal triangle built into a two-dimensional list.
    :type blueprint: list[list[int]]
    :rtype: None
    """

    # determines how far to push pyramid away from the leftmost edge of the console.
    if len(blueprint) < 4:
        width = len(blueprint) * (len(blueprint))
    elif len(blueprint) < 20:
        width = len(blueprint) * (len(blueprint) // 2)
    else:
        width = len(blueprint) * (len(blueprint) // 4)

    # iterate over each row and calculate custom padding for whitespace
    for row in blueprint:
        row = " ".join(map(str, row))  # break numbers out of the 2D-matrix
        padding = (width - len(row)) // 2  # the amount of " " to put on both sides
        print(" " * padding, row, " " * padding)  # print row with padding adjustment


def main() -> None:
    """
    This program will generate and print a pascal triangle with a given number of rows determined by the user. The user
    will input a non-negative integer number representing the desired amount of rows. The program will take that value
    and run an iterative algorithm to generate the triangle. A special function is called to format and output the
    result to the terminal.
    """

    # get int from user,
    total_rows = get_input()

    # pass the number to the generator function then call fuction to print the result.
    print_pascal_triangle(generate_pascal_triangle(total_rows))


main()
