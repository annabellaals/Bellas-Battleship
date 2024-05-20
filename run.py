import os, types
from typing import List

# Battleship class
class Battleship:
    def __init__(self, size, name) -> None:
        self.player_name = name

        # Variables denoting the characters
        self.ship = "@"
        self.target = "."
        self.bomb = "X"

        self.player_grid = [[self.target] * size] * size # Create the target grid as an array
        self.computer_grid = [[self.target] * size] * size # Create the target grid as an array

        self.clear()

    # Function to clear the terminal
    def clear(self):
        # Checks the os type and clears terminal accordingly
        if "nt" in os.name:
            os.system('cls')
        else:
            os.system('clear')

    # Function to display the grid
    def display(self):
        self.display_player()
        print()
        self.display_computer()

    # Player's grid display function
    def display_player(self):
        print(f"{self.player_name}'s board: ")
        
        for i in range(len(self.player_grid)):
            for j in range(len(self.player_grid[i])):
                print(self.player_grid[i][j], end="   ")
            print()

    # Computers's grid display function
    def display_computer(self):
        print("Computer's board: ")

        for i in range(len(self.computer_grid)):
            for j in range(len(self.computer_grid[i])):
                if self.player_grid[i][j] == self.bomb:
                    print(self.bomb, end="   ")
                else:
                    print(self.target, end="   ")
            print()

if __name__ == "__main__":
    # Get custom grid size
    grid_size = int(input("Enter grid size: "))
    name = input("Enter player name: ")

    # Play game
    battleship = Battleship(grid_size, name)
    battleship.display()
