# Calendar Display Program

This Python script utilizes the `calendar` module to display formatted calendar data for a specified month in the Gregorian calendar.

### Purpose

The program serves the following purposes:

1. **User Input Handling:**
   - Prompt users to enter a full month name found in the Gregorian calendar.
   - Validate the input against a predefined dictionary (`month_dict`).
   - Raise an exception if the entered month is not in the calendar.

2. **Calendar Display:**
   - Utilize the `calendar` module to display the calendar and additional information for the specified month.
   - Print the number of days in the month.

### Input

The program takes the following input:

- A full month name (e.g., January, january, JaNuAry) entered by the user when prompted.

### Expected Output

Upon successful execution, the program prints the formatted calendar for the specified month, including the number of days in the month.

```
==============================
    January 2023
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31

January had 31 days in 2023!
==============================
```

### Type of Execution

The program involves the following types of execution:

- **Sequential Execution:**
  - The main function (`main()`) orchestrates the flow, calling other functions sequentially.

- **Exception Handling (Conditional Execution):**
  - The program handles exceptions when the entered month is not found in the predefined dictionary (`month_dict`).

### Potential Improvements

The program could be enhanced in the following ways:

1. **Input Flexibility:**
   - Allow users to input abbreviated month names for increased flexibility.

2. **Year Flexibility:**
   - Allow users to specify the year for which they want to display the calendar.
