import os, types
from typing import List

# Function to display the grid
def display_grid(grid: List[List[str]]):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end="\t")
        print('\n')

# Get custom grid size
grid_size = int(input("Enter grid size: "))

grid = [[f"X"] * grid_size] * grid_size # Create the grid as an array

display_grid(grid)
