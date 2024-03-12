"""
Author: Jalen Vaughn
Date: 3/7/2024
File: probability.py
Description: This script is the solution to problem one in assignment 7.
Imports: itertools
"""

from itertools import product


class Utils:
    """
    This class contains utility/helper functions.
    """
    
    @staticmethod
    def print_header(header=None) -> None:
        """
        Prints a header to the console with a given text inside
        :param header: Optional string to use for the text inside the header.
        """
        
        if header is None:
            print("=" * 50)
            return
        
        # calculate the correct amount of "=" and dead space to properly fit header in the center
        width: int = 50  # total size
        padding: int = (width - len(header)) // 2  # the amount of "=" signs to put on both sides
        print("=" * padding, header, "=" * padding)


def probability(dice_config: str, threshold: int) -> str:
    """
    Calculates the probability of a die roll at and above the specified threshold.
    :param str dice_config: The dice configuration in the format "NdS" where N is the number of dice and S is the number
     of sides.
    :param int threshold: The number to calculate the probability at and above.
    :return: String formatted probability of the dice roll.
    :raises ValueError: If the dice configuration cannot exist.
    :raises TypeError: If the arguments are not of the correct type.
    """
    # Catch argument errors
    if type(dice_config) is not str:
        raise TypeError("Dice configuration must be a string\nconsisting of two positive integers "
                        "delimited by \"d\".")
    elif type(threshold) is not int:
        raise TypeError("Threshold must be an integer.")
    
    # Catch errors and validate the dice_config input
    try:
        # Split dice_config by the delimiter into two integer variables
        num_dice, num_sides = map(int, dice_config.split("d"))
    except ValueError as e:
        raise e
    
    # Prevent divide by zero error
    if num_sides <= 0:
        raise ValueError("A zero sided dice configuration cannot exist.")
    
    # Calculate the total amount of combinations in the set
    total_events: int = num_sides ** num_dice
    
    # Generate a set of all possible combinations
    sample_space: product[tuple[int, ...]] = product(range(1, num_sides + 1), repeat=num_dice)
    
    # Iterate through the set. The count of events in the sample space that meet the threshold requirement are
    # summed up and declared as target_events
    target_events: int = sum(sum(e) >= threshold for e in sample_space)
    
    # Return the chances of rolling at or above the threshold
    return f"{target_events / total_events * 100:.2f}% or {target_events} / {total_events}"


def main():
    """
    Main entry point of the program. Each test case within the program will run through the probability function and
    print the result.
    """
    test_cases = [
        ('2d6', 7),
        ('2d6', 9),
        ('3d8', 22),
        ('1d20', 17),
        (6, 5)
    ]
    
    # Run parameters through the probability function
    for dc, t in test_cases:
        Utils.print_header(f"Test: {dc}, {t}")
        print(probability(dc, t))
    else:
        Utils.print_header()


main()
