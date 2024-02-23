# Statistics Calculator

**Author:** Jalen Vaughn  
**Date:** 2/20/24  
**File:** main.py

## Description

This module contains the solution for Question 1 on Assignment 6. It provides a Statistics class capable of calculating
the mean, median, and range of a series of numbers generated within a specified range and step size. Additionally, it
includes functionality to obtain user input for defining the range and step size of the series.

## Purpose

The purpose of this program is to perform statistical calculations on a series of numbers generated within a specified
range and step size. It calculates the mean, median, and range of the generated series.

## Input

The program takes the following inputs:

- Lower boundary: Start point of the series.
- Upper boundary: End point of the series (inclusive).
- Step size: The increment/decrement between each value in the series.

## Expected Output

The program outputs the following statistical characteristics of the generated series:

- Values: The list of generated values.
- Mean: The arithmetic mean of the values.
- Median: The median value of the values.
- Range: The range of the values.

```
================== Lower Boundary ==================
Enter an integer: 1
================== Upper Boundary ==================
Enter an integer: 10
==================== Step Size ====================
Positive steps start at 1 and end at 10, inclusive.
Negative steps start at 10 and end at 1, inclusive.
==================================================
Enter an integer: -1
================== Statistic Info ==================
Values: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Mean: 5.50
Median: 5.50
Range: 9
```
## Classes

![image](https://github.com/jvspeed74/B210/assets/74921563/7108d6e6-b9ef-4d7f-8b8e-424d1438712e)

## Execution Type

The program utilizes a procedural programming style. It follows a linear flow, obtaining user input, validating it,
performing calculations, and displaying the results.

Specific Types:
- Sequential
- Conditional
- Repeated

## Potential Improvements

- Error Handling: Enhance error handling to provide more informative messages for users.
- Performance Optimization: Optimize the algorithm for generating the series and calculating statistics, especially for
  larger datasets.
- Additional Statistics: Expand the functionality to include more statistical measures beyond mean, median, and range.
