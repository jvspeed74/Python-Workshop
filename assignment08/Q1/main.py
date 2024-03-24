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
    def print_header(text=None, decor="=") -> None:
        """
        Prints a header to the console with a given text inside
        :param text: Optional var to use for the text inside the header.
        :param decor: Optional str to replace "=" with a custom item
        """
        
        # Print header without text.
        if text is None:
            print(decor * 50)
            return
        
        # Declare header margins.
        width: int = 50
        padding: int = (width - len(text)) // 2
        
        # Print header with text.
        print(decor * padding, text, decor * padding)


def count_types(string: str) -> None:
    """
    This function takes a string as input, and will calculate the number of numeric characters, lower case characters,
    upper case characters, and symbols contained in the string and displays them to the user. Use string functions to
    make the display aesthetically pleasing.
    :param string: String to be iterated upon.
    """
    
    # Declare variables that will count the varying character types.
    numeric_count, lowercase_count, uppercase_count, symbol_count = 0, 0, 0, 0
    
    # Iterate over the string.
    for char in string:
        # Check character type and update counter.
        if char.isnumeric():
            numeric_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        elif not char.isalnum():
            symbol_count += 1
    
    # Format and display answer.
    print(f"Numeric Characters: {numeric_count}")
    print(f"Lowercase Characters: {lowercase_count}")
    print(f"Uppercase Characters: {uppercase_count}")
    print(f"Symbols: {symbol_count}")


def main():
    """
    Main entry point of the program. Each test case within the program will run through the count_types function and
    print the result.
    """
    
    # Declare test cases.
    test_cases: list[str] = [
        "n<V}wePdAA`9kE2?",
        'u@jmzB="nMLLH6Ee',
        "K}s?3UdG_t:m=+Wz",
        "N7pKt`N/Y2Pcr/mS",
        "K^5Vk&EA!?`6aB@$",
    ]
    
    # Test the count_types function.
    for string in test_cases:
        Utils.print_header(f"Test: {string}")
        count_types(string)
    else:
        Utils.print_header()


main()
