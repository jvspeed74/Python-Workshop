"""
Author: Jalen Vaughn
Date: 3/7/2024
File: probability.script.py
Description: 
Imports: 
"""

import numpy as np


def probability(dice_config: str, threshold: int) -> float:
    num_of_dice, num_of_sides = map(int, dice_config.split("d"))
    
    # todo base case
    if num_of_dice == 1:
        return 1 / 6
    
    return np.array([[x + y for x in range(1, num_of_sides + 1)] for y in range(1, num_of_sides + 1)])

def main() -> None:
    print(probability(dice_config="3d8", threshold=7))


main()
