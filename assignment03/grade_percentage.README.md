# Assignment 3 - Question 1

# Grade Calculator

`grade_percentage.py` is a Python script designed to facilitate the calculation of letter grades based on user-provided
percentage inputs.

### Purpose

The program serves the following purposes:

1. **Input Validation:**
    - Prompt users to enter a grade percentage as a decimal between 0 and 1 (inclusive).
    - Validate the input and handle potential errors.

2. **Grade Calculation:**
    - Calculate and print the corresponding letter grade based on predefined percentage bands.

### Input

The program takes the following input:

- A grade percentage as a decimal entered by the user when prompted.

### Expected Output

Upon successful execution, the program prints the calculated letter grade corresponding to the user-provided percentage.

#### Test cases

```pycon
Input -> Output
---------------
0.75 -> "Grade: C" 

75 -> "Invalid percentage: '75' => Value between 0 and 1 expected."

0.8995 -> "Grade: B+"

-0.25 -> "Invalid percentage: '-0.25' => Value between 0 and 1 expected."

A -> "Invalid input: 'A' => Expected input consisting of only number and decimal characters."
```

### Type of Execution

The program involves the following types of execution:

- **Sequential Execution:**
    - The main function orchestrates the flow, calling other functions sequentially.

- **Conditional Execution:**
    - The `calculate_letter_grade` function uses conditional statements to determine the appropriate letter grade based
      on the input percentage.

### Potential Improvements

The program could be enhanced in the following ways:

1. **Improved Input Handling:**
    - The introduction of a 'While True' loop would allow for users to attempt multiple inputs without the script exiting abruptly.

2. **Flexibility in Input Format:**
    - Allow users to input grades in percentage format (e.g., 85%) in addition to decimal form.
