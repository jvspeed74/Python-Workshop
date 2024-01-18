Assignment 1
= 

There are two programs in this submission:

- Change Calculator (USD)
- Temperature Conversion (Celcius, Fahrenheit, Kelvin)

Change Calculator
===========

Purpose
------------


Solve or estimate the amount of change when given the amount tendered and total cost of a transaction.

Inputs
---

These values are obtained by prompting the user for manual entry.

- Tender Amount
- Cost of Item

````
        # get user input
        tender = float(input("Enter amount tendered in dollars"))
        cost = float(input("Enter the cost of item"))
````


Expected Outputs
---

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

Type of Execution (Pseudocode)
---


> // Pseudocode  
> **While True:**  
> Try to get and convert user input  
> Throw exception if input is negative **OR** non-numeric  
> Else perform calculation and print result  
> Prompt user to end script
> 


Error Handling
---

Negative entries input by user are caught in a conditional. This will print an exception statement and continue (restart)
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


Possible Improvements
---

