"""
Author: Jalen Vaughn
Date: 3/7/2024
File: main.py
Description: This script is the solution to problem 2 in assignment 7
Imports: 
"""
from itertools import permutations


def combinatorics(sequence: str) -> list[tuple[str, ...]]:
    """
    This function creates a list of permutations of a given string. Note: f-strings or any arbitrary strings will throw
    an exception.
    :param str sequence: The item to create permutations of.
    :return: A list of permutations
    :raises TypeError: If the sequence is not a string.
    """
    
    try:  # Validate argument type
        if type(sequence) is not str:
            raise TypeError("Sequence must be a string")
        
        # Generate a list of permutations from the input sequence
        res: list[tuple[str, ...]] = list(permutations(sequence))  # TODO: Combine each elem into a string
    
    except TypeError as e:
        raise e
    else:
        return res


def main() -> None:
    """
    Main entry point of the program. Each test case within the program will run through the combinatorics function and
    print the result.
    :return:
    """
    test_cases = [
        "ABC",
    ]
    
    # Run parameter through the combinatorics function
    for s in test_cases:
        print(combinatorics(s))


main()
