# Probability Calculator

## Purpose

The purpose of this program is to calculate the probability of rolling a die at or above a specified threshold, given a
certain dice configuration.

## Imports

- From `itertools` import `product`
- From `time` import `sleep`

## Input

- `dice_config`: A string representing the dice configuration in the format "NdS" where N is the number of dice and S is
  the number of sides.
- `threshold`: An integer representing the threshold number.

## Expected Output

The program returns a string formatted probability of rolling the dice at or above the specified threshold.

```
================== Test: 1d20, 17 ==================
20.00%
==================== Test: 6, 5 ====================
Program Error: Dice configuration must be a string
consisting of two positive integers delimited by "d"
==================================================
```

## Execution

- Conditional
- Repeated
- Sequential

## Potential Improvements

1. **Algorithm Optimizations**: Optimizing list generation techniques.

2. **In-depth Testing**: More test cases could be added to ensure the robustness of the program.

3. **Greater Functionality**: The script could be extended to handle more complex dice configurations, such as adding
   modifiers or special rules.
