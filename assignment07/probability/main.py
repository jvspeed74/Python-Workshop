"""
Author: Jalen Vaughn
Date: 3/7/2024
File: probability.script.py
Description: 
Imports: 
"""

import numpy as np
from scipy.stats import norm, triang, mode
from itertools import product


class Utils:
    """
    This class contains utility/helper functions.
    """
    
    @staticmethod
    def print_error(msg=None) -> None:
        """
        Prints an error message
        :param msg: Error message to print
        """
        
        Utils.print_header("Program Error")
        if msg is not None:
            print(msg)
    
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


def probability(dice_config: str, threshold: int):
    """
    Calculates the probability of a die roll at and above the specified threshold
    :param str dice_config: The dice configuration in the format "NdS" where N is the number of dice and S is the number
     of sides
    :param int threshold: The number of the target threshold to calculate at and above.
    :return:
    """
    try:
        if type(dice_config) is not str:
            raise ValueError("Dice configuration must be a string consisting of two numbers delimited by \"d\"")
        elif type(threshold) is not int or threshold < 0:
            raise ValueError("Threshold must be a positive integer")
        
        num_dice, num_sides = map(int, dice_config.split("d"))
    
    except ValueError as e:
        Utils.print_error()
        return e
    else:
        
        total_events = num_sides ** num_dice
        
        sample_space = product(range(1, num_sides + 1), repeat=num_dice)
        
        possible_events = sum(sum(e) >= threshold for e in sample_space)
        
        return possible_events / total_events * 100


def main():
    print(probability("52d6", "6"))


main()
