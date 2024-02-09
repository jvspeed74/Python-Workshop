# TODO: Add documentation for script and readme
import cipher_module as cm


def main():
    # TODO: Add decorators to program

    # initialize library handler and text scraper functionality
    text_scraper = cm.TextScraper()
    while True:
        text_scraper.set_active_text()
        text_scraper.set_active_char()
        print(text_scraper.get_char_count())
        break


main()
