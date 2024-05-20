import os, types
from typing import List

# Battleship class
class Battleship:
    def __init__(self, size) -> None:
        self.grid = [[f"X"] * size] * size # Create the grid as an array

    # Function to display the grid
    def display(self):
        # Check os type and clear terminal 
        if "nt" in os.name:
            os.system('cls')
        else:
            os.system('clear')

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                print(self.grid[i][j], end="   ")
            print()

if __name__ == "__main__":
    # Get custom grid size
    grid_size = int(input("Enter grid size: "))

    # Play game
    battleship = Battleship(grid_size)
    battleship.display()
