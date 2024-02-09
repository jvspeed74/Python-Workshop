__title__ = 'Cipher'
__summary__ = 'This module is built to assist with cipher analysis of a given text.'
__author__ = 'Jalen Vaughn'
__url__ = ''  # TODO: ADD GITHUB URL


class PassageManager:
    def __init__(self):
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

    def display_library(self):
        for k in self.library.keys():
            print(k)


class TextScraper(PassageManager):
    def __init__(self):
        super().__init__()
        self.active_text: str = ""
        self.active_char: str = ""

    def set_active_text(self):
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

    def set_active_char(self):
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

    def get_char_count(self) -> int:
        # Call the passage from the library and return the count the character appears
        return self.library[self.active_text].count(self.active_char)
