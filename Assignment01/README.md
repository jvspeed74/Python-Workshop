Assignment 1
= 

There are two programs in this submission:

- Change Calculator (USD)
- Temperature Conversion (Celcius, Fahrenheit, Kelvin)

# Change Calculator

### Purpose

This script calculates the change for a transaction and denotes the required amount of each dollar and coin.

### Type of Execution (Pseudocode)

> 1. Initialize denominations
> 2. Declare test cases
> 3. Calculate change
> 4. Split change dollars and coins into separate integers
> 5. Find minimum amount of dollars/coins using recursion
> 6. Print the answer

### Functions
```pycon
get_change(tender, cost)
    """
    Calculates the difference between tender and cost
    :param float tender:
    :param float cost:
    :return: tender minus cost rounded to two decimal places
    :rtype: float
    """
```

```pycon
get_minimum_amount(value, deno, memo=None)
    """
    Finds the minimum amount of the set denomination required to reach zero using recursion
    :param int value: Remaining change to find the minimum amount for
    :param list deno: List of the denominations to use for recursion
    :param dict memo: Memoization dictionary used to store results
    :return: Dictionary with the count of each required denomination
    :rtype: dict
    """
```
```pycon
get_answer(dollar_dict, coin_dict)
    """
    Formats and prints the minimum amount of dollars and coins
    :param dict dollar_dict: Dictionary containing required dollar information
    :param dict coin_dict: Dictionary containing required coin information
    """
```
```pycon
main()
    """
    Iterates through test cases and prints the minimum amount of dollars and coins required.
    """
```


### Inputs

The script takes the following inputs:

- Tender: The amount tendered in the transaction.
- Cost: The total cost of the transaction.

The denominations for dollars and coins are predefined within the script.

### Expected Outputs

For each test case, the script outputs:

- Tender amount
-  Cost
- Calculated change
- The minimum number of bills and coins required for the change

### Error Handling

There are no error handling mechanisms found in the script. The test cases are guaranteed to work.

### Possible Improvements

- Implementation of more test cases to understand where bugs arise.

# Temperature Conversion

### Purpose

Calculate the temperature for the given scale.

### Inputs

- Fahrenheit: float = 98.6
- Kelvin: float = 329.7
- Celsius: float = -60.9

### Expected Outputs

- Fahrenheit to Celsius conversion
- Kelvin to Fahrenheit conversion
- Celsius to Kelvin conversion

The output is formatted in a compound statement where the conversion result is printed, then followed up
with the temperature type. 

```pycon
print(ans1, "degrees Celsius")
print(ans2, "degrees Fahrenheit")
print(ans3, "degrees Kelvin")
```

The final output of the program:

```
37.0 degrees Celsius
134.06 degrees Fahrenheit
212.1 degrees Kelvin
```

### Types of Execution (Pseudocode)

> Declare variables based from conversion formulas  
> Display answers

### Error Handling
- None

### Possible Improvements

Each conversion type can be initialized in their own functions. This allows for code reuse
by reducing the amount of hardcoded statements. Memory is also reduced slightly since each function can return
the answer directly without declaring additional variables.
