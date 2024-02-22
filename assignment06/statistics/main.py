"""
Name: Jalen Vaughn
Date: 2/20/24
File: main.py
Description: This module contains the solution for Question 1 on Assignment 6.
Dependencies/Imports: 
"""


# TODO: ADD DOCUMENTATION AND COMMENTS

class Statistics:
    def __init__(self, lower_bound, upper_bound, step_size):
        self.values = [x for x in range(lower_bound, upper_bound + 1, abs(step_size))]
        
        if step_size < 0:
            self.values = sorted(self.values, reverse=True)
    
    def mean(self) -> float:
        return sum(self.values) / len(self.values)
    
    def median(self) -> float | int:
        if len(self.values) % 2 == 0:
            return (self.values[len(self.values) // 2] + self.values[(len(self.values) // 2) - 1]) / 2
        else:
            return self.values[(len(self.values) // 2)]
    
    def range(self) -> int:
        return max(self.values) - min(self.values)
    
    def display_stats(self) -> None:
        return print(f"Values: {self.values}\n"
                     f"Mean: {self.mean():.2f}\n"
                     f"Median: {self.median():.2f}\n"
                     f"Range: {self.range()}")


def input_int() -> int:
    """
    Gets an input from the user and returns the value if it is a validated float.
    :return: Extracted value from the user.
    :rtype: int
    """
    while True:
        user_input = input("Enter an integer: ")
        
        try:
            user_input = int(user_input)
        except ValueError:
            print(f"Invalid input: '{user_input}'. Your input is not a valid integer.")
            continue
        
        # valid float
        return user_input


def print_header(header=None) -> None:
    """
    Prints a header to the console with a given text inside
    :param header: Optional string to use for the text inside the header.
    """
    if header is None:
        print("=" * 50)
    
    else:  # calculate the correct amount of "=" and dead space to properly fit header in the center
        width = 50  # total size
        padding = (width - len(header)) // 2  # the amount of "=" signs to put on both sides
        print("=" * padding, header, "=" * padding)


def main():
    while True:
        # declare boundaries
        print_header("Lower Boundary")
        lower_bound = input_int()
        
        print_header("Upper Boundary")
        while True:
            upper_bound = input_int()
            
            # Logic error: Lower boundary cannot be greater than Upper
            if lower_bound >= upper_bound:
                print(f"Invalid input: {upper_bound}\nUpper bound must be greater than lower bound: {lower_bound}")
                continue
            
            break
        
        print_header("Step Size")
        print(f"Positive values start at {lower_bound} and end at {upper_bound}, inclusive.")
        print(f"Negative values start at {upper_bound} and end at {lower_bound}, inclusive.")
        print_header()
        while True:
            step_size = input_int()
            
            # Logic error: Impossible to step by zero
            if step_size == 0:
                print(f"Invalid input: {step_size}\nStep size cannot be zero.")
                continue
            
            break
        
        # Validation error: Length of list must be at least 3
        if lower_bound + abs(step_size * 2) > upper_bound:
            print("Error: The combination of boundaries and step size leads to a list that is too small.\n"
                  "Please enter a new set of values.")
            continue
        
        # Create Statistic object and display results
        stats = Statistics(lower_bound, upper_bound, step_size)
        print_header("Statistics")
        stats.display_stats()

        # end program
        break

main()
