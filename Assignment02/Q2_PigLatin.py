def convert_to_piglatin(word: str) -> None:
    """
    Prints an input word converted to piglatin.
    Every vowel before the first consonant is moved to the end of the word.
    Every word is appended with "ay"
    :param word:
    """

    # decorator and script formatting
    print("=" * 15)
    print(f"Word: {word}")
    print(f"Piglatin: ", end="")

    # declare variables
    vowels = ['a', 'e', 'i', 'o', 'u']  # letters to skip
    stack = ''  # stack of skipped letters

    # loop through characters
    for i in range(len(word)):

        # return if letter not a vowel
        if word[i] not in vowels:
            return print(word[i:] + stack + "ay")

        # add letter to stack
        stack += word[i]

    # all letters in word are vowels
    print(word + "ay")


def main():
    convert_to_piglatin("simple")
    convert_to_piglatin("friends")
    convert_to_piglatin("omelet")
    convert_to_piglatin("ions")


main()
