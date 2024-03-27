"""
Name: Jalen Vaughn
Date: 3/26/24
File: main.py
Description: This script contains the solution to question 1
Dependencies/Imports: Numpy
"""
# todo add comments and docstuff
import numpy as np


class SudokuValidator:
    def __init__(self, grid):
        self.grid = grid
    
    @property
    def grid(self):
        return self._grid
    
    @grid.setter
    def grid(self, new_grid):
        def is_valid():
            if isinstance(new_grid, list):
                if len(new_grid) == 9:
                    return True
                elif all(isinstance(subgrid, list) and len(subgrid) == 3 for subgrid in new_grid):
                    return True
            return False
        
        if is_valid():
            self._grid = new_grid
        else:
            raise TypeError(f"Invalid input '{new_grid}'. Expected a flat list of 9 elements or a 3x3 matrix.")
    
    def check_legality(self):
        matrix = np.array(self._grid, ndmin=2)
        memory = {}
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                try:
                    int_value = int(matrix[i, j])
                except ValueError:
                    print(f"Non-integer value '{matrix[i, j]}' found at row {i} and column {j}")
                else:
                    if not 1 <= int_value <= 9:
                        print(f"Illegal value '{int_value}' found at row {i} and column {j}."
                              f"Values must be integers in the range 1-9.")
                    elif int_value in memory:
                        print(f"Duplicate value '{int_value}' found at row {i} and column {j}")
                    else:
                        memory[int_value] = (i, j)


def main():
    # Declare test cases
    test_cases = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [[5, 3, 4], [6, 7, 2], [1, 9, 8]],
        [[9, 9, 2], [3, 4, 8], [5, 6, 7]],
        [[8, 5, 9], [4, 2, 6], [8, 1, 3]],
        [[7, 6, 1], [6, 8, 5], [3, 9, 6]],
        [[4, 2, "E"], [7, 9, "I"], [8, "S", 6]],
        [[6, 7, 8], [1, 9, 5, 3], [3, 4, 2]]
    ]
    
    # Call each test case and display result
    for test in test_cases:
        test_obj = SudokuValidator(test)
        test_obj.check_legality()


main()
