# Permutation Generator

## Purpose:

This Python script generates permutations of a given string using the `itertools.permutations` function. It provides
a `combinatorics` function that takes a string as input and returns a list of permutations of that string. The main
function demonstrates the usage of the `combinatorics` function by running test cases and printing the results.

## Imports:

- From `itertools` import `permutation`

## Input:

The program takes a single input: a string representing the sequence for which permutations are to be generated.

## Output:

The expected output of the program is a list of permutations of the input string. Each permutation is represented as a
string.

```
['Hi!', 'H!i', 'iH!', 'i!H', '!Hi', '!iH']
```

## Execution:

- Conditional
- Repeated
- Sequential

## Potential Improvements:

1. **Error Handling Improvement**: The error handling in the `combinatorics` function could be improved to provide more
   informative error messages or handle specific cases more gracefully.

2. **User Interface**: Adding a user interface could make the program more user-friendly, allowing users to input
   strings interactively and view the permutations directly without modifying the script.
