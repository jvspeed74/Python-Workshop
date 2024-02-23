"""
Name: Jalen Vaughn
Date: 2/20/24
File: main.py
Description: This module contains the solution for Question 2 on Assignment 6.
Dependencies/Imports: None
"""


def print_header(header=None) -> None:
    """
    Prints a header to the console with a given text inside
    :param header: Optional string to use for the text inside the header.
    """
    if header is None:
        print("=" * 50)
    
    else:  # calculate the correct amount of "=" and dead space to properly fit header in the center
        width = 50  # total size
        padding = (width - len(header)) // 2  # the amount of "=" signs to put on both sides
        print("=" * padding, header, "=" * padding)


def main() -> None:
    """
    Main function of the program mean to fulfill the script purpose:
    1. Obtain the secret message via user input.
    2. Iterate through the message while simultaneously validating and decrypting the values.
    3. Print out the decoded message to the terminal.
    """
    # welcome message
    print_header("Cryptography")
    print("This program will help you decrypt a secret message.\n"
          "The message should be composed of:\n"
          "- A list of integers separated by spaces")
    
    # start program flow
    print_header("Decode Message")
    while True:
        # get encoded user input and split into list
        secret_message: list[str] = input("Enter a string of integers separated by spaces: ").split(" ")
        
        # decode each list number while validating input
        decoded_text: list = []
        for n in secret_message:
            
            # convert number to integer; will throw ValueError if unable
            try:
                n: int = int(n)
            except ValueError:
                print(f"Non-integer detected: {n}\nExpected a list of integers separated by a single space.")
                break
            
            # if number is positive, convert to octal form
            if n >= 0:
                n: int = int(oct(n)[2:])  # eject "0o" from the value and convert back to int
            
            # validate n to a positive number and append character representation
            decoded_text.append(chr(abs(n)))
        else:
            # combine list items into a string then print the result
            print_header("Result")
            print("".join(decoded_text))
            
            # end program
            break


main()
