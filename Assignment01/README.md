Assignment 1
= 

There are two programs in this submission:

- Change Calculator (USD)
- Temperature Conversion (Celcius, Fahrenheit, Kelvin)


# Change Calculator


### Purpose



Solve or estimate the amount of change when given the amount tendered and total cost of a transaction.

### Inputs


These values are obtained by prompting the user for manual entry.

- Tender Amount
- Cost of Item

````
        # get user input
        tender = float(input("Enter amount tendered in dollars"))
        cost = float(input("Enter the cost of item"))
````

### Expected Outputs


The user will be presented with two separate strings varying on certain conditions being met.

````
        # conditional to assess output
        if change < 0:
            print("You don't have enough money to buy this item")
        else:
            print("Your change is $"'{:.2f}'.format(change))
````

If the amount tendered is less than the cost of the item, then the user doesn't have enough money to purchase the item.
Otherwise, the change is displayed in a logical format (two decimal points).

### Type of Execution (Pseudocode)



> // Pseudocode  
> **While True:**  
> Try to get and convert user input  
> Throw exception if input is negative **OR** non-numeric  
> Else perform calculation and print result  
> Prompt user to end script
>


### Error Handling


Negative entries input by user are caught in a conditional. This will print an exception statement and continue (
restart)
onto the next iteration of the while loop.

````
        # error handling if negative
        if tender < 0 or cost < 0:
            print("Cannot compute negative numbers")
            continue
````

Non-numeric characters are caught in a try, except execution. An error message will display and the program will
continue onto the next iteration.

```
    try:
        # get user input
        tender = float(input("Enter amount tendered in dollars"))
        cost = float(input("Enter the cost of item"))
```

```
    # error handling if non-numerical characters entered
    except ValueError:
        print("Please enter numerical characters")
        continue
```

### Possible Improvements


The program can be split into modular components AKA functions. This would make the debugging process easier. Prompting
the user for inputs can lead to longer execution times. It would be quicker to store all values of tender and cost in
separate arrays and iterate through them simultaneously.

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
