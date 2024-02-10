# Cipher

## Purpose

The `cipher.py` script serves two main purposes:

1. **Passage Manager**: Stores passages along with their titles and provides a method to display available passages.
2. **Text Scraper**: Allows users to search for a specific character within a selected passage and returns the count of
   occurrences.

## Input

The program takes the following inputs:

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

## Overview of Classes and Functions

- **PassageManager**: Manages passages and provides methods to display passage titles.
    - __init__(): Initializes the library of passages.
    - display_library(): Prints out the titles of available passages.
- **TextScraper**: Inherits from PassageManager and allows searching for characters within passages.
    - __init__(): Initializes attributes related to the active text and character.
    - set_active_text(): Sets the active text based on user input.
    - set_active_char(): Sets the active character based on user input.
    - search_char(): Counts the occurrences of the active character within the active text.
    - get_char_count(): Returns the count of character occurrences.
    - get_active_text(): Returns the title of the active text.
    - get_active_char(): Returns the active character.
- **print_header()**: Prints a header with a given text.

## Potential Improvements

1. The ability to add, edit, or delete passages in the library.
2. Scanning the passage for the count of all characters in a sorted array.
