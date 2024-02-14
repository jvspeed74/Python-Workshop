"""
Name: Jalen Vaughn
Date: 2/13/24
File: main.py
Description: Script to build a pascal triangle
Dependencies:
    - print_header() from utils.py: Used to display customized headers in console.
"""

from utils import print_header
from typing import List


def get_input() -> int:
    """
    Gets user input and type casts it to int.
    :return: A positive integer
    :rtype: int
    """
    while True:
        # get input
        user_input = input("Enter a positive integer: ")

        # error handle conversion to integer
        try:
            user_input = int(user_input)

        # catch error
        except ValueError:
            print(f"Invalid number: '{user_input}'. Input must be an integer.")
            continue

        # check if input is negative
        if user_input <= 0:
            print("Please enter a positive integer.")
            continue

        if user_input < 1:
            print("A pyramid without any rows isn't really a pyramid, is it?")
            continue

        # validated integer
        return user_input


def pascal_triangle(n_rows: int) -> List[List[int]] | int:
    """
    Builds a pascal triangle with the given number of rows.
    :param n_rows: number of rows valued at 1 or more.
    :type n_rows: int
    :return: A pascal triangle built into a compounded list.
    :rtype: List[List[int]]
    """

    res = [[1]]

    current_row = []
    for i in range(n_rows - 1):
        next_row = [1]
        for j in range(i + 1):
            # reached the end of the row
            if j == i:
                next_row.append(1)
                break

            next_row.append(current_row[j] + current_row[j + 1])

        current_row = next_row.copy()
        res.append(current_row)

    return res


def display_pascal_triangle(blueprint: List[List[int]]) -> None:
    pass


def main():
    pass


# main()


print(pascal_triangle(1000))

