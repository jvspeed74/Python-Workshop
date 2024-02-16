"""
Name: main.py

Note: This program was originally in three separate files for clarity purposes. They have been combined into one file to
prevent grading discrepancies.

There are three sections in this script:
1. Classes
2. Helper Functions / Utilities
3. The Main Function
"""


# **********************************************************************************************************************
#
# The next section is dedicated to classes that provide library management and text scraping abilities.
#
# **********************************************************************************************************************
class PassageManager:
    """
    Manages passages and provides methods to display passage titles.
    """

    def __init__(self):
        # passage storage
        self.library = {
            "The Raven": "Open here I flung the shutter, when, with many a flirt and flutter, In there stepped a stately "
                         "Raven of the saintly days of yore; Not the least obeisance made he; not a minute stopped or stayed "
                         "he; But, with mien of lord or lady, perched above my chamber door— Perched upon a bust of Pallas "
                         "just above my chamber door— Perched, and sat, and nothing more.",
            "Fire and Ice": "Some say the world will end in fire, Some say in ice. From what I’ve tasted of desire I hold "
                            "with those who favor fire. But if it had to perish twice, I think I know enough of hate To say "
                            "that for destruction ice Is also great And would suffice.",
            "Awaking in New York": "Curtains forcing their will against the wind, children sleep, exchanging dreams with "
                                   "seraphim. The city drags itself awake on subway straps; and I, an alarm, awake as a rumor "
                                   "of war, lie stretching into dawn, unasked and unheeded.",
            "I'm thankful that my life doth not deceive": "I’m thankful that my life doth not deceive Itself with a low "
                                                          "loftiness, half height, And think it soars when still it dip its "
                                                          "way Beneath the clouds on noiseless pinion Like the crow or owl, "
                                                          "but it doth know The full extent of all its trivialness, "
                                                          "Compared with the splendid heights above. See how it waits to "
                                                          "watch the mail come in While ’hind its back the sun goes out "
                                                          "perchance. And yet their lumbering cart brings me no word, "
                                                          "Not one scrawled leaf such as my neighbors get To cheer them with "
                                                          "the slight events forsooth, Faint ups and downs of their far "
                                                          "distant friends— And now ’tis passed. What next? See the long "
                                                          "train Of teams wreathed in dust, their atmosphere; Shall I attend "
                                                          "until the last is passed? Else why these ears that hear the "
                                                          "leader’s bells Or eyes that link me in procession? But hark! the "
                                                          "drowsy day has done its task, Far in yon hazy field where stands a "
                                                          "barn, Unanxious hens improve the sultry hour And with contented "
                                                          "voice now brag their deed— A new laid egg—Now let the day decline— "
                                                          "They’ll lay another by tomorrow’s sun.",
        }
        self.titles = [k.lower() for k in self.library.keys()]  # used for case-sensitive comparisons

    def display_library(self) -> None:
        """
        Prints out the title of each passage in a list format.
        """
        print("Library:")
        for k in self.library.keys():
            print("- ", k)

        print_header()

    def add_new_passage(self):
        """
        A title and text of a new passage is extracted from user and added as an entry in the library.
        """
        print_header("New Passage")

        # title loop
        while True:
            # get input
            input_title = input("Enter a Title: ")

            # prevent 'Add' or empty string from being used as a title
            if not input_title or input_title.capitalize() == 'Add':
                print("This title cannot exist within the library")
                continue

            # if title already exists
            if input_title.lower() in self.titles:
                print("This passage already exists in the library.")
                continue

            # title valid
            break

        # text loop
        while True:
            # get input
            input_text = input("Enter the passage text (must be over 200 characters): ")

            # verify correct length
            if len(input_text) < 200:
                print(f"Text length must be at least 200: [Missing {200 - len(input_text)} characters]")
                continue

            # text valid
            break

        # add to library and update titles
        self.library[input_title] = input_text
        self.update_titles()

    def update_titles(self):
        """
        Updates the titles list based off the current keys in the library.
        """
        self.titles = [k.lower() for k in self.library.keys()]


class TextScraper(PassageManager):
    """
    Inherits from PassageManager and allows searching for characters within passages.
    """

    def __init__(self):
        super().__init__()
        self.passage: str = ""  # passage being search through
        self.character: str = ""  # character being searched for
        self.char_count: int = 0  # amt of times character appears in passage

    def set_passage(self) -> None:
        """
        Sets the passage attribute to a passage name in the library. Also allows the user to input their own passage.
        """
        while True:
            print_header("Select Text")
            # get options
            self.display_library()

            # get input
            user_input = input("Enter a passage name or 'Add' to add your own: ")

            # add passage if requested
            if user_input.capitalize() == "Add":
                self.add_new_passage()
                continue

            # check if in dict and try again if not
            if not self.library.get(user_input, False):
                print(f"Unable to find {user_input} in library.")
                continue

            # key exists in library
            break

        # set value
        self.passage = user_input
        print_header(self.passage)

    def set_character(self) -> None:
        """
        Sets the character to an extracted value of user input.
        """
        while True:
            # get input
            user_input = input("Enter a character to look for: ")

            # check if it's a single character
            if len(user_input) != 1:
                print("Please enter a single character.")
                continue

            # input valid
            break

        # set value
        self.character = user_input

    def search_passage(self) -> None:
        """
        Call the passage from the library and counts the amount of times the character appears. The value is
        stored in the char_count attribute.
        """
        self.char_count = self.library[self.passage].count(self.character)

    def print_result(self) -> None:
        """
        Prints the result in a specific format that calls the character, passage, and char_count attributes.
        """
        print_header("Result")
        print(f"'{self.character}' occurs {self.char_count} time(s) in {self.passage}")

    def get_char_count(self) -> int:
        """
        Getter: self.char_count
        :return: the amount of times the character appears in the text
        :rtype: int
        """
        return self.char_count


# **********************************************************************************************************************
#
# The next section is dedicated to helper functions or utilities not directly related to the main purpose of the script.
#
# **********************************************************************************************************************
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


# **********************************************************************************************************************
#
# The next section is dedicated to the main function that runs the entire script.
#
# **********************************************************************************************************************
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


main()
