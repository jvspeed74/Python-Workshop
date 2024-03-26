"""
Name: Jalen Vaughn
Date: 3/26/24
File: main.py
Description: This script contains the solution to question 1
Dependencies/Imports: None
"""
from typing_extensions import a

class Subgrid:
    def __init__(self, grid: list[list[int]]):
        self.grid = grid
    
    def is_matrix(self):
        pass
    
    def is_list(self):
        pass


def main():
    test = Subgrid([[5, 3, 4], [6, 7, 2], [1, 9, 8]])
    print(test.validate())


main()
