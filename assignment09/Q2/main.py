"""
Name: Jalen Vaughn
Date: 3/26/24
File: main.py
Description: This script contains the solution to question 2
Dependencies/Imports: None
"""


class Utils:
    """
    This class contains utility/helper functions.
    """
    
    @staticmethod
    def print_header(text=None, decor="=", width=50) -> None:
        """
        Prints a header to the console with a given text inside
        :param text: Optional var to use for the text inside the header.
        :param decor: Optional str to replace "=" with a custom item
        :param width: Optional int to set the width of the header.
        """
        
        # Print header without text.
        if text is None:
            print(decor * width)
            return
        
        # Declare header margins.
        padding: int = (width - len(text)) // 2
        
        # Print header with text.
        print(decor * padding, text, decor * padding)


def word_count(text: str, most_common: bool = False) -> None:
    """
    Count the occurrences of each unique word in the given text.
    
    :param text: The input text to analyze.
    :param most_common: If True, display the three most common words and their counts.
    """
    # Catch invalid arguments.
    if not isinstance(text, str) or not isinstance(most_common, bool):
        raise TypeError(f"Invalid input")
    
    bank: dict = {}  # Stores each word (key) and the number of occurrences (value).
    
    # Check each word in text (case-insensitive) and store the number of occurrences in dict.
    for word in text.split():
        if word.lower() in bank:
            bank[word.lower()] += 1
        else:
            bank[word.lower()] = 1
    
    # Display results; Check for optional param.
    print("Number of unique words:", len(bank))
    if most_common:
        # Grab the top 3 words from the word bank and print them to the terminal.
        sorted_bank = sorted(bank.items(), key=lambda x: x[1], reverse=True)
        print("Most common words:")
        for word, count in sorted_bank[:3]:
            print(f"- '{word.capitalize()}' appeared {count} times")


def main():
    """
    Main entry point of the program. Each test case will be passed through the word_count function.
    """
    
    # Declare list of test inputs
    test_cases = ["""It was many and many a year ago
In a kingdom by the sea
That a maiden there lived whom you may know
By the name of Annabel Lee
And this maiden she lived with no other thought
Than to love and be loved by me""",
                  """I was a child and she was a child
In this kingdom by the sea
But we loved with a love that was more than love
I and my Annabel Lee
With a love that the winged seraphs of Heaven
Coveted her and me""",
                  """And this was the reason that long ago
In this kingdom by the sea
A wind blew out of a cloud chilling
My beautiful Annabel Lee
So that her highborn kinsmen came
And bore her away from me
To shut her up in a sepulchre
In this kingdom by the sea""",
                  """The angels not half so happy in Heaven
Went envying her and me
Yes that was the reason as all men know
In this kingdom by the sea
That the wind came out of the cloud by night
Chilling and killing my Annabel Lee""",
                  """But our love it was stronger by far than the love
Of those who were older than we
Of many far wiser than we
And neither the angels in Heaven above
Nor the demons down under the sea
Can ever dissever my soul from the soul
Of the beautiful Annabel Lee""",
                  """For the moon never beams without bringing me dreams
Of the beautiful Annabel Lee
And the stars never rise but I feel the bright eyes
Of the beautiful Annabel Lee
And so all the night-tide I lie down by the side
Of my darling my darling my life and my bride
In her sepulchre there by the sea
In her tomb by the sounding sea""",
                  ]
    
    # Call each test and display result
    for i, test in enumerate(test_cases):
        Utils.print_header(f"Stanza #{i + 1}")
        word_count(test, True)
    else:
        Utils.print_header("Entire Poem")
        word_count(''.join(test_cases), True)


main()
