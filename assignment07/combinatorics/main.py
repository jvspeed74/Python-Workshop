"""
Author: Jalen Vaughn
Date: 3/7/2024
File: main.py
Description: This script is the solution to problem 2 in assignment 7
Imports: 
"""
from itertools import permutations


class Utils:
    """
    This class contains utility/helper functions.
    """
    
    @staticmethod
    def print_header(header=None) -> None:
        """
        Prints a header to the console with a given text inside
        :param header: Optional string to use for the text inside the header.
        """
        
        if header is None:
            print("=" * 50)
            return
        
        # Calculate the correct amount of "=" and dead space to properly fit header in the center
        width: int = 50  # Total size
        padding: int = (width - len(header)) // 2  # The amount of "=" signs to put on both sides
        print("=" * padding, header, "=" * padding)


def combinatorics(sequence: str) -> list[str]:
    """
    This function creates a list of permutations of a given string. Note: f-strings or any arbitrary strings will throw
    an exception.
    :param str sequence: The item to create permutations of.
    :return: A list of permutations
    :raises TypeError: If the sequence is not a string.
    """
    
    # Validate argument type
    if type(sequence) is not str:
        raise TypeError("Sequence must be a string")
    
    # Generate a list of permutations from the input sequence
    permutation_list: permutations[str] = permutations(sequence)
    
    # Format the result into a list of string
    res: list[str] = [''.join(perm) for perm in permutation_list]
    
    return res


def main():
    """
    Main entry point of the program. Each test case within the program will run through the combinatorics function and
    print the result.
    """
    
    # Declare test cases
    test_cases = [
        "ABC",
    ]
    
    # Run parameter through the combinatorics function
    for s in test_cases:
        Utils.print_header(f"Test: {s}")
        print(combinatorics(s))
    else:
        Utils.print_header()


main()
