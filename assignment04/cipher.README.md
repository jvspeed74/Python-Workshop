# Cipher

## Purpose

The `cipher.py` script serves two main purposes:

1. **Passage Manager**: Stores passages along with their titles and provides a method to display available passages.
   Users are able to add passages with select constraints.
2. **Text Scraper**: Allows users to search for a specific character within a selected passage and returns the count of
   occurrences.

## Input

The program takes the following inputs:

- The title and text of a new passage.
- Selection of a passage title from the available library.
- A single character to search for within the chosen passage.

## Expected Output

Upon successful execution, the program returns the count of occurrences of the specified character within the selected
passage.

```
=================== Select Text ===================
Options:
-  The Raven
-  Fire and Ice
-  Awaking in New York
-  I'm thankful that my life doth not deceive
==================================================
Enter the passage name to search: Fire and Ice
=================== Fire and Ice ===================
Enter a character to search for f
====================== Result ======================
Your character 'f' occurs 9 time(s)
```

## Type of Execution

- Sequential Execution
- Conditional Execution
- Repeated Execution

```plantuml

class PassageManager {
    -library: dict
    -titles: list
    +__init__()
    +display_library(): None
    +add_new_passage(): None
    +update_titles(): None
}

class TextScraper {
    -passage: str
    -character: str
    -char_count: int
    +__init__()
    +set_passage(): None
    +set_character(): None
    +search_passage(): None
    +print_result(): None
    +get_char_count(): int
}


class Functions << (F,#FF7700) >> {
    +print_header(): None
}

class Main << (M, #00DAD0) >> {

}

PassageManager --> Functions : Uses
TextScraper --> Functions : Uses
TextScraper --|> PassageManager : Inherits
Main --> TextScraper : Uses
Main --> Functions : Uses




```


## Overview of Classes and Functions

### Classes

- **PassageManager**: Manages passages and provides methods to display passage titles.
    - __init__(): Initializes the library of passages.
    - display_library(): Prints out the titles of available passages.
    - add_new_passage(): Adds a user inputted passage to the library.
    - update_titles(): Reads the current keys in the library and updates the titles accordingly.


- **TextScraper**: Inherits from PassageManager and allows searching for characters within passages.
    - __init__(): Initializes attributes related to the active text and character.
    - set_passage(): Sets the active text based on user input.
    - set_character(): Sets the active character based on user input.
    - search_passage(): Counts the occurrences of the active character within the active text.
    - get_char_count(): Returns the count of character occurrences.

### Functions

  - print_header(): Prints a header with a given text.

## Potential Improvements

1. The ability to edit, or delete passages in the library.
2. Scanning the passage for the count of multiple characters.
3. Displaying a sorted array of all character occurrences.
