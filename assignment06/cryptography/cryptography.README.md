# Cryptography

**Author:** Jalen Vaughn  
**Date:** 2/20/24  
**File:** main.py

## Description

This module contains a Python script designed to decrypt a secret message encoded with a specific cipher. The script
allows users to input a list of numbers, which represent encrypted characters. It then decrypts the message by
converting each number to its corresponding ASCII character, with some numbers being first converted to octal form.

## Purpose

The purpose of this program is to decode a secret message encrypted using a combination of decimal and octal values. It
provides a simple interface for users to input the encoded message and decrypt it into readable text.

## Input

The program takes a string of numbers separated by spaces as input. These numbers represent the encrypted characters of
the secret message.


## Expected Output

The expected output of the program is the decrypted message, which is printed to the terminal after decoding the input
numbers.

```
Enter a string of numbers separated by spaces: 57 73 73 64
Good
```

## Execution Type

The program follows a procedural execution style. It prompts the user for input, performs decryption, and outputs the
decoded message.

Specific Types:
- Sequential
- Conditional
- Repeated

## Potential Improvements

- Code Refactoring: Consider refactoring the code for readability and maintainability, breaking down complex sections
  into smaller functions.
- Encoding Ability: Implement functionality that gives the user the ability to encode their own message.
