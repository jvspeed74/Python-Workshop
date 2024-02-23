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
        for elem in secret_message:
            
            # convert number to integer; will throw ValueError if unable
            try:
                num: int = int(elem)
            except ValueError:
                print(f"Non-integer detected: {elem}\nExpected a list of integers separated by a single space.")
                break
            
            # convert to octal form -> slice "0o" -> get chr from value
            if num >= 0:
                decoded_text.append(chr(int(oct(num)[2:])))
            
            # leave in dec form -> turn value positive -> get chr from value
            else:
                decoded_text.append(chr(abs(num)))
        
        else:
            # combine list items into a string then print the result
            print_header("Result")
            print("".join(decoded_text))
            
            # end program
            break


main()
