# Assignment 1 - Question 2

# Pig Latin Converter

`PigLatin.py` defines a function `convert_to_piglatin` that takes an input word and prints its Pig Latin equivalent. The program demonstrates the usage of this function in the `main` function with sample words.

### What is the purpose of this program?

The program aims to convert input words into Pig Latin. It follows the Pig Latin rules by continuously moving the leading character to the end of the word
    until the character being moved is a consonant, then appending "ay" to the end.

### What does this program take as input?

The program takes a single parameter:

- `word`: (Required) The word to be converted to Pig Latin.

### What is the expected output of the program?

The program prints the original word and its Pig Latin equivalent for each input, formatted for readability.

```
===============
Word: simple
Piglatin: implesay
===============
```

### What type of execution is included in your program?

- Sequential Execution
- Conditional Execution  
- Repeated Execution

### How could your program be improved?

- Handling uppercase letters and maintaining the case in the Pig Latin output.
- Including validation for the input word (e.g., ensuring it is not empty and contains alphabetic characters).
- Providing an option to process multiple words in a sentence.
- Error handling for words that consist entirely of vowels.
