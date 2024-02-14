# Pascal Triangle Generator

## Overview

This Python script generates a Pascal triangle based on user input. The
program employs dynamic programming to construct the triangle efficiently. It takes the number of rows as input from the
user and prints the resulting Pascal triangle to the console.

### Files

- `main.py`: Contains the main script and the direct code required for successful processing.

## Functionality

- **get_input()**: Prompts the user to enter the number of rows for Pascal's Triangle and validates the input.
- **generate_pascal_triangle(n_rows)**: Constructs a Pascal triangle with the specified number of rows using a bottom-up
  dynamic programming approach.
- **print_pascal_triangle(blueprint)**: Formats and prints the Pascal triangle to the console in a pyramid shape.
- **main()**: Orchestrates the execution of the program by using function calls to get user input, generate the
  Pascal triangle, and print the result.

## Input

The program takes a non-negative integer input from the user representing the desired number of rows for Pascal's
Triangle.

## Expected Output

Upon execution, the program prints the Pascal triangle to the console. Each row of the triangle is combined to display
in a pyramid shape, centered horizontally, with appropriate whitespace padding.

```
Enter the number of rows for Pascal's Triangle: 5
     1     
    1 1    
   1 2 1   
  1 3 3 1  
 1 4 6 4 1 
```

## Execution

- Sequential
- Conditional
- Repeated

## Potential Improvements

1. **Efficiency**: Optimize the algorithm for generating the Pascal triangle by reducing space complexity.
    - Implementing Numpy and Deque to reduce data structure processing power.
2. **Flipping the Shape**: Include the ability of the user inputting a negative number to flip the shape of the
   pyramid.
