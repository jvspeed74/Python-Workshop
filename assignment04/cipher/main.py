"""
Name: main.py
Description: The main program of the module
Imports: TextScraper class from passage_manager; print_header function from utils
"""
from passage_manager import TextScraper
from utils import print_header


def main():
    """
    Main Program:
    1. Creates a TextScraper object, which is a subclass of PassageManager, that allows you to search for
    character occurrence in a passage.
    2. Prompts user to select a passage name and a single character to observe. Or grants the user to add a passage of
    their own.
    3. If the specified character is unable to be found, the program will prompt the user to enter another character.
    4. The program will display the amount of times the character occurs and end.
    """

    # welcome statement
    print_header("Cipher")
    print("Welcome! This program allows the user to enter a    \n"
          "passage name and a single character. The number of  \n"
          "times the character appears is calculated and       \n"
          "displayed! A new feature is the ability to add your \n"
          "own passage to the library. See below :D")

    # initialize library handler and text scraper
    text_scraper = TextScraper()

    # prompt user for passage name
    text_scraper.set_passage()

    # infinite loop: repeats until a character is found in text
    while True:
        # get char from user and search text
        text_scraper.set_character()
        text_scraper.search_passage()

        # check if character doesn't occur
        if not text_scraper.get_char_count():
            print("Character not found in text. Try another!")
            continue

        # all requirements met
        text_scraper.print_result()
        break


if __name__ == "__main__":
    main()
