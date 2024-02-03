def convert_to_piglatin(word: str) -> None:
    """
    Converts a word to Pig Latin by continuously moving the leading character to the end of the word
    until the character being moved is a consonant.

    :param word:
    """

    # decorator and script formatting
    print("=" * 20)
    print(f"Word: {word}")
    print(f"Piglatin: ", end="")

    # declare variables
    vowels = ['a', 'e', 'i', 'o', 'u']  # letters to skip
    stack = ''  # stack of skipped letters

    # loop through characters
    for i in range(len(word)):

        # add letter to stack
        stack += word[i]

        # if letter moved to stack is a consonant
        if word[i] not in vowels:
            # print(rest of the word + letters previously iterated through + "ay")
            print(word[i + 1:] + stack + "ay")
            return


def main():
    """
    Four test cases, which are english words, are passed into the convert_to_piglatin function.
    The results get displayed as a consecutive output sequence.
    A closing wrapper is attached after the final function call.
    """
    convert_to_piglatin("simple")
    convert_to_piglatin("friends")
    convert_to_piglatin("omelet")
    convert_to_piglatin("ions")
    print("=" * 20)


main()
