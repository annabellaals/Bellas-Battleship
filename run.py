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

        self.round = 0

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

    # Function that displays stats after every round
    def transmission(self, phit, pcords, chit, ccords):
        self.clear()
        pstr = "did" if phit else "did not"
        cstr = "did" if chit else "did not"
        
        print(f"Round {self.round}")
        print(f"---{self.player_name} attacked: ({pcords[0]}, {pcords[1]})")
        print(f"---{self.player_name} {pstr} hit a ship!")
        print(f"---Computer attacked: ({ccords[0]}, {ccords[1]})")
        print(f"---Computer {cstr} hit a ship!")

        print(f"Player: {self.size - self.computer_ship_count - 1}\t\tComputer: {self.size - self.player_ship_count - 1}")

        input("\nPress enter to continue...")

    # Main gameloop
    def play(self):
        while self.computer_ship_count > 0 or self.player_ship_count > 0:
            player_hit = computer_hit = False
            self.display()
            
            # First take user input
            crow = int(input("Enter row: "))
            ccol = int(input("Enter col: "))

            # Attack computer
            if self.computer_grid[crow][ccol] == self.ship:
                self.computer_ship_count -= 1
                computer_hit = True

            self.computer_grid[crow][ccol] = self.bomb
            
            # Do the same for computer
            prow = random.randint(0, self.size-1)
            pcol = random.randint(0, self.size-1)

            # Attack player
            if self.player_grid[prow][pcol] == self.ship:
                self.player_ship_count -= 1
                player_hit = True

            self.player_grid[prow][pcol] = self.bomb

            self.round += 1
            self.transmission(computer_hit, (crow, ccol), player_hit, (prow, pcol))
           
    # Function to display the grid
    def display(self):
        self.clear()
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


