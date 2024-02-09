from passage_data import passages


class TextScraper:
    def __init__(self, data):
        self.library: dict = data
        self.active_text: str = ""
        self.active_char: str = ""

    def set_active_text(self):
        # get input
        while True:
            user_input = input("Enter the passage name to search ")

            # check if in dict and try again if not
            if not self.library.get(user_input, False):
                print("Error")
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
                print("Error")
                continue

            # input valid
            break

        # set value
        self.active_char = user_input

    def get_char_count(self) -> int:
        return self.library[self.active_text].count(self.active_char)


def main():
    text_scraper = TextScraper(passages)
    while True:
        text_scraper.set_active_text()
        text_scraper.set_active_char()
        print(text_scraper.get_char_count())
        break


main()
