"""
Name: Jalen Vaughn
Date: 2/13/24
File: main.py
Description: Script to get all the prime numbers within a range of numbers.
"""


def get_input() -> int:
    """
    Gets user input and type casts it to int.
    :return: A positive integer
    :rtype: int
    """

    while True:
        # get input
        user_input = input("Enter an endpoint (positive integer): ")

        # error handle conversion to integer
        try:
            user_input = int(user_input)

        # catch error
        except ValueError:
            print(f"Invalid number: '{user_input}'. Input must be an integer.")
            continue

        # check if input is negative
        if user_input < 0:
            print("Please enter a positive integer.")
            continue

        # validated integer
        return user_input


def generate_prime_list(endpoint: int) -> list[int]:
    """
    Generates a list of prime numbers between 2 and the endpoint parameter, inclusive.
    :param endpoint: The endpoint of the band of numbers checked by the function.
    :type endpoint: int
    :return: A list of prime numbers
    :rtype: list[int]
    """

    # two lists: one of the prime numbers and another of the multiples
    prime_list, multiple_list = [], []

    # iterate band of numbers until the endpoint.
    for n in range(2, endpoint + 1):

        # if multiple list is empty or if n is smaller than any multiple
        if not multiple_list or n < min(multiple_list):
            # add number to list of primes
            prime_list.append(n)

            # Everytime a prime number is added to list, n*n is added to multiples
            multiple_list.append(n * n)
            continue

        # if n is equal to any multiple, multiple += prime (corresponding)
        while n in multiple_list:
            multiple_list[multiple_list.index(n)] += prime_list[multiple_list.index(n)]

    return prime_list


def print_header(header=None) -> None:
    """
    Prints a header to the console with a given text inside
    :param header: Optional string to use for the text inside the header.
    """
    if header is None:
        print("=" * 60)

    else:  # calculate the correct amount of "=" and dead space to properly fit header in the center
        width = 60  # total size
        padding = (width - len(header)) // 2  # the amount of "=" signs to put on both sides
        print("=" * padding, header, "=" * padding)


def main() -> None:
    """
    This program inputs a integer from the user. The integer is used as an endpoint in a band of numbers starting with
    two. The script outputs a list of prime numbers up to the endpoint, inclusive.
    :rtype: None
    """

    # start
    print_header("Prime Number Generator")
    print("This script will generate a prime number list.\n"
          "The list will run until a user specified endpoint, inclusive.")

    # get int from user
    print_header("Endpoint Selection")
    endpoint = get_input()

    # generate prime list, display results, and end script.
    print_header("Result")
    print(f"Prime numbers: {generate_prime_list(endpoint)}")


main()
