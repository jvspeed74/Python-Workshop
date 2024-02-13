"""
Name: Jalen Vaughn
Date: 2/13/24
File: main.py
Description: Script to get all the prime numbers within a range of numbers.
Dependencies:
- print_header() from utils.py: Used to display customized headers in console.
TODO: Add readme documentation for prime.README.md
"""
from utils import print_header


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

        # validated integer
        return user_input


def generate_prime_list(endpoint: int) -> None:
    """
    Generates a list of prime numbers between 2 and the endpoint parameter, inclusive.
    :param endpoint: The endpoint of the band of numbers checked by the function.
    :type endpoint: int
    :rtype: None

    Notes:
    - Two lists: one of the prime numbers and another of the multiples
    - Everytime a prime number is added to list, n*n is added to multiples
    - primes and mult have the same index
    - if n is smaller than any multiple, add to list of primes
    - if n is equal to any multiple, multiple += prime (corresponding)
    """

    # base case: No prime numbers are below 2.
    if endpoint < 2:
        print("There are no prime numbers less than 2.")
        return

    # two lists: one of the prime numbers and another of the multiples
    prime_list, multiples = [], []

    # iterate band of numbers until the endpoint.
    for n in range(2, endpoint + 1):

        # if multiple list is empty or if n is smaller than any multiple
        if not multiples or n < min(multiples):

            # add number to list of primes
            prime_list.append(n)

            # Everytime a prime number is added to list, n*n is added to multiples
            multiples.append(n * n)
            continue

        # if n is equal to any multiple, multiple += prime (corresponding)
        while n in multiples:
            multiples[multiples.index(n)] += prime_list[multiples.index(n)]

    print(f"Prime numbers: {prime_list}")


def main() -> None:
    """
    This program inputs a integer from the user. The integer is used as an endpoint in a band of numbers starting with
    two. The script outputs a list of prime numbers up to the endpoint, inclusive.
    :rtype: None
    """

    # start
    print_header("Prime Number Generator")

    # get int from user
    endpoint = get_input()

    # generate prime list, display results, and end script.
    print_header("Result")
    generate_prime_list(endpoint)


main()
