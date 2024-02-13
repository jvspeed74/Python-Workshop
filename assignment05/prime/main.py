"""
Name: Jalen Vaughn
Date: 2/13/24
File: main.py
Description: Script to get all the prime numbers within a range of numbers.
Dependencies/Imports: 
"""
from utils import print_header


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


def find_prime_num(endpoint: int):
    pass


def main():
    pass
