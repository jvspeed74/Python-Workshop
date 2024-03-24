"""
Name: Jalen Vaughn
Date: 3/21/24
File: main.py
Description: This script contains the solution to question 2
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


def decode_acrostic(acrostic: str, first_line: int = 0, char_start_pos: int = 0, delimiter: str = "\n") -> None:
    """
    Decodes an acrostic poem and prints the result.
    :param acrostic: The acrostic poem string.
    :param first_line: The starting position for iterating through lines (optional).
    :param char_start_pos: The starting position for iterating through characters in each line (optional).
    :param delimiter: The character that separates lines in the acrostic poem (optional).
    """
    
    # Split acrostic string by its delimiter.
    acrostic_list: list[str] = acrostic.split(sep=delimiter)
    
    # Iterate over each line and append the first alphabetic character to the output.
    secret_message: str = ""
    for line in acrostic_list[first_line:]:
        for char in line[char_start_pos:]:
            # Ensure we grab the first alphabetic character.
            if char.isalpha():
                secret_message += char
                break
    
    # Display the result to the user.
    print(secret_message)


def main():
    """
    Main entry point of the program. Each test case within the program will run through the decode_acrostic function and
    display the result.
    """
    
    # Declare test cases.
    test_set_a = [
        ["SATOR\nAREPO\nTENET\nOPERA\nROTAS\n"],
    ]
    
    test_set_b = [
        ['Elizabeth it is in vain you say\t'
         '“Love not” – thou sayest it in so sweet a way:\t'
         'In vain those words from thee or L.E.L.\t'
         'Zantippe’s talents had enforced so well:\t'
         'Ah! If that language from thy heart arise,\t'
         'Breath it less gently forth — and veil thine eyes.\t'
         'Endymion, recollect, when Luna tried\t'
         'To cure his love – was cured of all beside\t'
         'His folly – pride – and passion – for he died.']
    ]
    
    # Test decode_acrostic function.
    # Test Set A
    Utils.print_header("Starting Test A", "*")
    for test in test_set_a:
        for i in range(5):  # Test Indexes 0-4.
            Utils.print_header(f"Test A: {i + 1}")
            decode_acrostic(*test, char_start_pos=i)
    else:
        Utils.print_header("Test A Complete", "*")
        
    # Test Set B
    Utils.print_header("Starting Test B", "*")
    for counter, test in enumerate(test_set_b):
        Utils.print_header(f"Test B: {counter + 1}")
        decode_acrostic(*test, delimiter="\t")
    else:
        Utils.print_header("All Tests Complete", "*")


main()
