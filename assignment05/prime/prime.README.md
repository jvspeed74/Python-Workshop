# Prime Number Generator

## Overview

This Python script aims to generate a list of prime numbers within a specified range. It prompts the user to input an
endpoint, which determines the upper limit of the range of numbers to check. The script then identifies all prime
numbers within this range and outputs them to the console.

### Files

- `main.py`: Contains the main script and the direct code required for successful processing.

## Functionality

- **get_input()**: Retrieves user input, validates it, and ensures it is a positive integer.
- **generate_prime_list(endpoint)**: Generates a list of prime numbers between 2 and the specified endpoint, inclusive.
- **print_header()**: Prints a customer header to the console.
- **main()**: Orchestrates the execution of the program, prompting the user for input, generating the prime number list,
  and displaying the result.

## Input

The program takes a single positive integer as input, which represents the endpoint of the range of numbers to check for
prime numbers.

## Expected Output

Upon execution, the program prints the list of prime numbers within the specified range to the console.

```
========================== Prime Number Generator ==========================
This script will generate a prime number list.
The list will run until a user specified endpoint, inclusive.
============================ Endpoint Selection ============================
Enter an endpoint (positive integer): 10
================================== Result ==================================
Prime numbers: [2, 3, 5, 7]
```

## Execution

- Sequential
- Conditional
- Repeated

## Potential Improvements

1. **Efficiency**: Optimize the algorithm for generating prime numbers.
