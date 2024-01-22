Assignment 1
= 

There are two programs in this submission:

- Change Calculator (USD)
- Temperature Conversion (Celcius, Fahrenheit, Kelvin)


# Change Calculator


### Purpose



Solve or estimate the amount of change when given the amount tendered, the total cost of a transaction, as well as the
dollars/coins needed for the transaction.  

### Type of Execution (Pseudocode)

> 

### Inputs


### Expected Outputs








### Error Handling


### Possible Improvements



# Temperature Conversion

### Purpose

Calculate the temperature for the given scale

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

```
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
