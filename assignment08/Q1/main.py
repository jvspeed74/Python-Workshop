"""
Name: Jalen Vaughn
Date: 3/21/24
File: main.py
Description: This script contains the solution to question 1
Dependencies/Imports: None
"""


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


def count_types(string: str) -> None:
    """
    This function takes a string as input, and will calculate the number of numeric characters, lower case characters,
    upper case characters, and symbols contained in the string and displays them to the user. Use string functions to
    make the display aesthetically pleasing.
    
    :param string: String to be iterated upon.
    """
    if type(string) is not str:
        raise TypeError("Error in `count_types`: Argument must be a string")
    
    # Declare variables that will track count of character types
    numeric_count: int = 0
    lowercase_count: int = 0
    uppercase_count: int = 0
    symbol_count: int = 0
    
    # Iterate over the string; incrementing counters where necessary
    for char in string:
        # Numeric check
        if char.isnumeric():
            numeric_count += 1
        
        # Lowercase check
        if char.islower():
            lowercase_count += 1
        
        # Uppercase check
        if char.isupper():
            uppercase_count += 1
        
        # Symbol check
        if not char.isalnum():
            symbol_count += 1
    
    # Format and display answer
    Utils.print_header("Count of Character Types")
    print(f"Numeric Characters: {numeric_count}")
    print(f"Lowercase Characters: {lowercase_count}")
    print(f"Uppercase Characters: {uppercase_count}")
    print(f"Symbols: {symbol_count}")


def main():
    """
    Main entry point of the program. Each test case within the program will run through the count_types function and
    print the result.
    """
    
    # Declare test cases
    test_cases: list[str] = [
        "n<V}wePdAA`9kE2?",
        'u@jmzB="nMLLH6Ee',
        "K}s?3UdG_t:m=+Wz",
        "N7pKt`N/Y2Pcr/mS",
        "K^5Vk&EA!?`6aB@$",
    ]
    
    # Run parameter through the count_types function
    for s in test_cases:
        Utils.print_header(f"Test: {s}")
        count_types(s)
    else:
        Utils.print_header()


main()
