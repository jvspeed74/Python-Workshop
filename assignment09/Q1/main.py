"""
Title: Sudoku Subgrid Checker
Name: Jalen Vaughn
Date: 3/26/24
File: main.py
Description: This script contains the solution to question 1
Dependencies/Imports: Numpy
"""
import numpy as np


class Utils:
    """
    This class contains utility/helper functions.
    """
    
    @staticmethod
    def print_header(text=None, decor="=", width=50) -> None:
        """
        Prints a header to the console with a given text inside
        :param text: Optional var to use for the text inside the header.
        :param decor: Optional str to replace "=" with a custom item
        :param width: Optional int to set the width of the header.
        """
        
        # Print header without text.
        if text is None:
            print(decor * width)
            return
        
        # Declare header margins.
        padding: int = (width - len(text)) // 2
        
        # Print header with text.
        print(decor * padding, text, decor * padding)


class SudokuSubgrid:
    """
    Represents a subgrid within a Sudoku puzzle.
    """
    
    def __init__(self, grid):
        self.grid = grid
    
    @property
    def grid(self):
        return self._grid
    
    @grid.setter
    def grid(self, new_grid) -> None:
        """
        Sets the grid attribute within the instance.
        
        :param new_grid: New grid (either 9 elements or a 3x3 matrix)
        :raises TypeError: If the input is invalid.
        """
        # Check if the input matches the required conditions.
        is_valid = False
        if isinstance(new_grid, list):
            if len(new_grid) == 9:
                is_valid = True
            elif all(isinstance(subgrid, list) and len(subgrid) == 3 for subgrid in new_grid):
                is_valid = True
        
        # Set attribute or raise error depending on is_valid flag.
        if is_valid:
            self._grid = new_grid
        else:
            raise TypeError(f"Invalid input '{new_grid}'. Expected a flat list of 9 elements or a 3x3 matrix.")
    
    def check_legality(self) -> None:
        """
        Checks the legality of the Sudoku subgrid.
        
        This method examines each cell in the subgrid and verifies whether the values meet the following criteria:
        1. Must be integers in the range 1-9.
        2. No duplicate values within the subgrid.
        """
        # Declare local variables
        matrix = np.array(self._grid, ndmin=2, dtype=str)  # Converts input array into a 2D matrix.
        illegal_reasons = []  # Stores strings that explain illegality.
        memory = {}  # Stores the cell value, and it's location within the matrix.
        
        # Check each cell value for legality.
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                try:  # Confirm that the cell value is an integer.
                    int_value = int(matrix[i, j])
                
                except ValueError:
                    illegal_reasons.append(f"Non-integer value '{matrix[i, j]}' found at row {i} and column {j}")
                
                else:  # Confirm the cell value is 1-9 and is not a duplicate value.
                    if not 1 <= int_value <= 9:
                        illegal_reasons.append(f"Illegal value '{int_value}' found at row {i} and column {j}. "
                                               f"Values must be integers in the range 1-9.")
                    elif int_value in memory:
                        illegal_reasons.append(f"Duplicate value '{int_value}' found at row {i} and column {j}")
                    else:
                        memory[int_value] = (i, j)
        
        # Print legality results.
        if illegal_reasons:
            print("The grid is illegal!")
            for i, reason in enumerate(illegal_reasons):
                print(f"{i + 1}: {reason}")
        else:
            print("The grid is legal.")


def main():
    """
    Main entry point of the program. Each test case will be passed through the SudokuSubgrid object, which initially
    checks that the input is correct. If correct, then the check_validity method is called on the input.
    """
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
    Utils.print_header("Starting Test", "*")
    for test in test_cases:
        print("\n")
        Utils.print_header(f"Test: {test}")
        try:
            test_obj = SudokuSubgrid(test)
            test_obj.check_legality()
        except Exception as e:
            print(e)
        
        Utils.print_header()
    else:
        Utils.print_header("All Tests Complete", "*")


main()
