# TODO: Add documentation for script and readme
import cipher_module as cm


def main():
    # TODO: Add decorators to program
    # welcome statement
    cm.print_section_header("Cipher")
    print("Welcome! This program takes two inputs:\n"
          "- The title of a passage in the library.\n"
          "- A character to scan the passage for.")

    # initialize library handler and text scraper functionality
    text_scraper = cm.TextScraper()

    cm.print_section_header("Select Text")
    text_scraper.set_active_text()

    # requirement loop: repeats until all conditions are met
    while True:
        cm.print_section_header(text_scraper.get_active_text())
        text_scraper.set_active_char()

        cm.print_section_header(text_scraper.get_active_text())
        text_scraper.search_char()

        if not text_scraper.get_char_count():
            print("Character not found in text. Try another!")
            continue

        print(f"Your character {text_scraper.get_active_char()} occurs {text_scraper.get_char_count()} time(s)")
        # all requirements met
        break


main()
