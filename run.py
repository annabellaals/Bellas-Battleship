import os
import random
from typing import List, Tuple

class Battleship:
    def __init__(self, size, name) -> None:
        self.player_name = name

        self.ship = "@"
        self.target = "."
        self.bomb = "X"

        self.size = size
        self.player_grid = [[self.target for _ in range(size)] for _ in range(size)]  
        self.computer_grid = [[self.target for _ in range(size)] for _ in range(size)]  

        self.player_ship_count = 0
        self.computer_ship_count = 0

        self.round = 0

        self.create_ships()
        self.clear()

    def create_ships(self):
        while self.player_ship_count < self.size - 1:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)

            if self.player_grid[row][col] == self.target:
                self.player_grid[row][col] = self.ship
                self.player_ship_count += 1

        while self.computer_ship_count < self.size - 1:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)

            if self.computer_grid[row][col] == self.target:
                self.computer_grid[row][col] = self.ship
                self.computer_ship_count += 1

    def clear(self):
        if "nt" in os.name:
            os.system('cls')
        else:
            os.system('clear')

    def transmission(self, phit, pcords, chit, ccords):
        self.clear()
        pstr = "did" if phit else "did not"
        cstr = "did" if chit else "did not"
        
        print(f"Round {self.round}: \n")
        print(f"---{self.player_name} attacked: ({pcords[0]}, {pcords[1]})")
        print(f"---{self.player_name} {pstr} hit a ship!\n")
        print(f"---Computer attacked: ({ccords[0]}, {ccords[1]})")
        print(f"---Computer {cstr} hit a ship!\n")

        print(f"Player: {self.size - self.computer_ship_count - 1}\tComputer: {self.size - self.player_ship_count - 1}")

        input("\nPress enter to continue...")
    
    def end_credits(self):
        self.clear()
        if self.player_ship_count == self.computer_ship_count:
            print("It was a tie!")
        elif self.player_ship_count < self.computer_ship_count:
            print("The computer won the game!")
        else:
            print(f"{self.player_name} won the game!")

    def play(self):
        while self.computer_ship_count > 0 and self.player_ship_count > 0:
            player_hit = computer_hit = False
            self.display()
            
            while True:
                try:
                    crow = int(input("Enter row: "))
                    ccol = int(input("Enter col: "))
                    if crow < 0 or crow >= self.size or ccol < 0 or ccol >= self.size:
                        print(f"Coordinates out of bounds. Please enter values between 0 and {self.size - 1}.")
                        continue
                    if self.computer_grid[crow][ccol] == self.bomb:
                        print("You've already bombed this location. Choose a different one.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
            
            if self.computer_grid[crow][ccol] == self.ship:
                self.computer_ship_count -= 1
                computer_hit = True

            self.computer_grid[crow][ccol] = self.bomb
            
            while True:
                prow = random.randint(0, self.size-1)
                pcol = random.randint(0, self.size-1)
                if self.player_grid[prow][pcol] != self.bomb:
                    break

            if self.player_grid[prow][pcol] == self.ship:
                self.player_ship_count -= 1
                player_hit = True

            self.player_grid[prow][pcol] = self.bomb

            self.round += 1
            self.transmission(computer_hit, (crow, ccol), player_hit, (prow, pcol))

        self.end_credits()
           
    def display(self):
        self.clear()
        self.display_player()
        print()
        self.display_computer()

    def display_player(self):
        print(f"{self.player_name}'s board: ")
        for row in self.player_grid:
            print("   ".join(row))
        print()

    def display_computer(self):
        print("Computer's board: ")
        for row in self.computer_grid:
            display_row = [self.bomb if cell == self.bomb else self.target for cell in row]
            print("   ".join(display_row))
        print()

if __name__ == "__main__":
    choice = -1

    while choice != 0:
        print("------BELLA'S BATTLESHIP------\n")
       
        while True:
            try:
                grid_size = int(input("Enter grid size: "))
                if grid_size >= 3 and grid_size <= 10:
                    break
                else:
                    print("Invalid choice. Please enter between 3 or 10.")
            except ValueError:
                print("Invalid input. Please enter 0 or 1.")

        name = input("Enter player name: ")

        battleship = Battleship(grid_size, name)
        battleship.play()

        while True:
            try:
                choice = int(input("\nEnter 0 to exit or 1 to play again: "))
                if choice in [0, 1]:
                    break
                else:
                    print("Invalid choice. Please enter 0 or 1.")
            except ValueError:
                print("Invalid input. Please enter 0 or 1.")
