def convert_to_piglatin(word: str) -> None:
    """
    Converts a word to Pig Latin by continuously moving the leading character to the end of the word
    until the character being moved is a consonant.
    :param word:
    """

    # decorator and script formatting
    print("=" * 30)
    print(f"Word: {word}")
    print(f"Piglatin: ", end="")

    # declare variables
    vowels = ['a', 'e', 'i', 'o', 'u']  # letters to skip
    stack = ''  # stack of skipped letters

    # loop through characters
    for i in range(len(word)):

        stack += word[i]

        # return if letter not in vowels
        if word[i] not in vowels:
            print(word[i+1:] + stack + "ay")
            break

    return


def main():
    convert_to_piglatin("simple")
    convert_to_piglatin("friends")
    convert_to_piglatin("omelet")
    convert_to_piglatin("ions")


main()
