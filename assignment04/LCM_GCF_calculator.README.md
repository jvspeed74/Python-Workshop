# LCM/GCF Calculator Program

### Purpose

This program calculates the Least Common Multiple (LCM) and Greatest Common Factor (GCF) of two integers provided by the
user. It offers flexibility in mode selection and ensures valid inputs.

### Input

The program takes the following inputs:

- Mode type (LCM or GCF) chosen by the user.
- Two integers entered by the user.

These inputs are case-insensitive in order to provide accessibility for users.

```pycon
if input("Enter 'Stop' to exit the script: ").upper() == 'STOP':
    print('Exiting... Goodbye!')
```

All string user inputs are converted to uppercase using the dot method `.upper()` before use in comparison operations.

### Expected Output

Upon successful execution, the program prints the result of the calculation based on the selected mode. It displays the
LCM or GCF of the provided integers.

```
====== Select Calculator Mode ======
Enter 'LCM' or 'GCF': gcf
============ Mode: GCF =============
Enter your first integer: 5
Enter your second integer: 18
============== Result ==============
The GCF for 18 and 5 is: 1
============= Continue? ============
Enter 'Stop' to exit the script: stop
Exiting... Goodbye!
```

### Type of Execution

The program involves the following types of execution:

- Sequential Execution
- Conditional Execution
- Repeated Execution
- Exception Handling
- Recursive Functionality

### Overview of Functions

- get_mode_type(): Prompts the user to select the mode type (LCM or GCF) and validates the input.
- get_two_int(): Prompts the user to enter two integers, validates the input, and returns them in a sorted list.
- calculate_LCM(a, b): Calculates the Least Common Multiple (LCM) of two integers using the standard formula.
- calculate_GCF(a, b): Calculates the Greatest Common Factor (GCF) of two integers using the Euclidean Algorithm.
- main(): Orchestrates the flow of the program by calling functions in order. Contains decorators via print statements.

### Potential Improvements

The program could be improved in the following ways:

1. Additional Numeric Inputs: Allow users to perform calculations on a integer count greater than two.
2. Standardized Decorator Functionality: Cleaning up `main()` by using Python's built-in configuration for decorators.
