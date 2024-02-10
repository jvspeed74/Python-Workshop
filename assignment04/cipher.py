class PassageManager:
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

    def display_library(self) -> None:
        """
        Prints out the title of each passage in a list format.
        """
        print("Options:")
        for k in self.library.keys():
            print("- ", k)

        print_header()


class TextScraper(PassageManager):
    def __init__(self):
        super().__init__()
        self.active_text: str = ""
        self.active_char: str = ""
        self.char_count: int = 0

    def set_active_text(self) -> None:
        """
        Sets the active text to user input corresponding to a passage name.
        """
        # get options
        self.display_library()

        # get input
        while True:
            user_input = input("Enter the passage name to search: ")

            # check if in dict and try again if not
            if not self.library.get(user_input, False):
                print(f"Unable to find {user_input} in library.")
                continue

            # key exists in library
            break

        # set value
        self.active_text = user_input

    def set_active_char(self) -> None:
        """
        Sets the active character to the extracted value of user input.
        """
        # get input
        while True:
            user_input = input("Enter a character to search for ")

            # check if it's a single character
            if len(user_input) != 1:
                print("Please enter a single character.")
                continue

            # input valid
            break

        # set value
        self.active_char = user_input

    def search_char(self) -> None:
        """
        Call the active text from the library and count the amount of times the active character appears. The value is
        stored in the character count attribute.
        """
        self.char_count = self.library[self.active_text].count(self.active_char)

    def get_char_count(self) -> int:
        return self.char_count

    def get_active_text(self) -> str:
        return self.active_text

    def get_active_char(self) -> str:
        return self.active_char


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


def main():
    """
    Main Program:
    1. Creates a TextScraper object, which is a subclass of PassageManager, that allows you to search for
    character occurrence in a passage.
    2. Prompts user to select a passage name and a single character to observe.
    3. If the specified character is unable to be found, the program will prompt the user to enter another character.
    Otherwise, the program will display the amount of times the character occurs and end.
    """
    # welcome statement
    print_header("Cipher")
    print("Welcome! This program takes two inputs:\n"
          "- The title of a passage in the library.\n"
          "- A character to scan the passage for.")

    # initialize library handler and text scraper
    text_scraper = TextScraper()

    # prompt user for passage name
    print_header("Select Text")
    text_scraper.set_active_text()
    print_header(text_scraper.get_active_text())

    # infinite loop: repeats until a character is found in text
    while True:
        # get char from user and search text
        text_scraper.set_active_char()
        text_scraper.search_char()

        # check if character doesn't occur
        if not text_scraper.get_char_count():
            print("Character not found in text. Try another!")
            continue

        # all requirements met
        print_header("Result")
        print(f"The character '{text_scraper.get_active_char()}' occurs {text_scraper.get_char_count()} time(s)")
        break


main()
