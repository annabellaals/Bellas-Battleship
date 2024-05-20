import os, types, random
from typing import List

# Battleship class
class Battleship:
    def __init__(self, size, name) -> None:
        self.player_name = name

        # Variables denoting the characters
        self.ship = "@"
        self.target = "."
        self.bomb = "X"

        self.size = size
        self.player_grid = [[self.target for _ in range(size)] for _ in range(size)]  # Create the target grid as an array
        self.computer_grid = [[self.target for _ in range(size)] for _ in range(size)]  # Create the target grid as an array

        self.player_ship_count = 0
        self.computer_ship_count = 0

        self.create_ships()
        self.clear()

    def create_ships(self):
        while self.player_ship_count + 1 < self.size:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)

            if self.player_grid[row][col] == self.target:
                self.player_grid[row][col] = self.ship
                self.player_ship_count += 1

        while self.computer_ship_count + 1 < self.size:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)

            if self.computer_grid[row][col] == self.target:
                self.computer_grid[row][col] = self.ship
                self.computer_ship_count += 1

    # Function to clear the terminal
    def clear(self):
        # Checks the os type and clears terminal accordingly
        if "nt" in os.name:
            os.system('cls')
        else:
            os.system('clear')

    # Main gameloop
    def play(self):
        while self.computer_ship_count > 0 or self.player_ship_count > 0:
            self.display()
            
            # First take user input
            prow = int(input("Enter row: "))
            pcol = int(input("Enter col: "))

            # Check if theres a ship present. Handle accordingly
            if self.player_grid[prow][pcol] == self.ship:
                self.player_ship_count -= 1

            self.player_grid[prow][pcol] = self.bomb

            # Do the same for computer
            crow = random.randint(0, self.size-1)
            ccol = random.randint(0, self.size-1)

            if self.computer_grid[crow][ccol] == self.ship:
                self.computer_ship_count -= 1

            self.computer_grid[crow][ccol] = self.bomb

    # Function to display the grid
    def display(self):
        self.display_player()
        print()
        self.display_computer()

    # Player's grid display function
    def display_player(self):
        print(f"{self.player_name}'s board: ")
        for row in self.player_grid:
            print("   ".join(row))
        print()

    # Computers's grid display function
    def display_computer(self):
        print("Computer's board: ")
        for row in self.computer_grid:
            display_row = [self.bomb if cell == self.bomb else self.target for cell in row]
            print("   ".join(display_row))
        print()

if __name__ == "__main__":
    # Get custom grid size
    grid_size = int(input("Enter grid size: "))
    name = input("Enter player name: ")

    # Play game
    battleship = Battleship(grid_size, name)
    battleship.play()


