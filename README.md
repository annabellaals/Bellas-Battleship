# README for Bella's Battleship

## Overview

Bella's Battleship is a command-line version of the classic board game "Battleship" written in Python. It provides an engaging single-player experience where the user competes against the computer, aiming to sink all of the opponent's ships before they sink yours.

![Gameplay](https://github.com/annabellaals/Bellas-Battleship/blob/main/images/2.png)

## How to Play

### Game Rules

- The player and the computer each have their own grid where ships are hidden.
- Players take turns bombing specific locations on the opponent's grid.
- The objective is to sink all of the opponent's ships.

### Steps to Play

1. **Start the Game**: Run the game in a Python environment.
2. **Enter Grid Size**: Input the size of the grid (between 3x3 and 10x10).
3. **Enter Player Name**: Provide your name for a personalized experience.
4. **Take Turns**: 
   - You will be prompted to enter the row and column for your attack.
   - The computer will randomly select a row and column to attack.
   - The game will notify you if a ship was hit or missed.
5. **End Game**: The game continues until all ships of one player are sunk. The winner is announced at the end.

### Example Usage

![](https://github.com/annabellaals/Bellas-Battleship/blob/main/images/1.png)

## Features

- **Customizable Grid Size**: Players can choose grid sizes between 3x3 and 10x10.
- **Random Ship Placement**: Ships are placed randomly on both player and computer grids.
- **Turn-Based Gameplay**: Players and the computer take turns to attack.
- **Input Validation**: Ensures valid coordinates are entered and prevents bombing the same location twice.
- **Round Feedback**: Provides feedback after each round on hits and misses.
- **Game Result**: Announces the winner at the end of the game.

## Technologies Used

The game implements several key technologies and concepts to create a fun and interactive environment

### 1. Python
- The game is written entirely in Python 3.12.1

### 2. Object Oriented Programming (OOP)
- The game uses OOP principles such as encapsulation and implements classes and objects. This promotes modularity and allows code reusage

### 3. Standard Libraries
- **random**: Used to generate random ship placement and computer's attacks
- **os**: Used to clear the console, providing a cleaner interface during gameplay

### 4. Game Logic and AI
- **Core Mechanics**: The game includes essential mechanics such as placement, attacking, processing the attacks and determining the end of game
- **Basic AI**: The computer's moves are generated randomly, implementing a simple yet effective artifical intelligence for the computer

### 5. User Interaction
- Players interact via the console by entering their name, grid size and attack coordinates
- The game provides feedback after every successful round by displaying the state, attack results and final scores

## Components and Their Descriptions

| Component       | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| `Battleship` Class | The main class that encapsulates the game logic, player and computer grids, and game state. |
| `__init__` Method | Initializes the game, sets up grids, and places ships randomly.            |
| `create_ships` Method | Randomly places ships on the player and computer grids.                   |
| `clear` Method | Clears the console screen for better user experience.                         |
| `transmission` Method | Displays the results of each round, including hits and misses.            |
| `end_credits` Method | Displays the final results of the game, announcing the winner.             |
| `play` Method | The main game loop that handles player and computer turns.                     |
| `display` Method | Displays the current state of the player and computer grids.                  |
| `display_player` Method | Displays the player's grid.                                              |
| `display_computer` Method | Displays the computer's grid, hiding ship locations.                    |
| `main` Script | Handles user inputs for grid size and player name, and starts the game.        |

## Testing

To test the game:
1. Run the script multiple times with different grid sizes.
2. Ensure all inputs are validated correctly.
3. Verify that the game correctly identifies hits, misses, and previously bombed locations.
4. Check the end-game conditions to ensure the correct winner is announced.

## Validator Testing

- Passed the [PEP 8 online validator](https://pep8ci.herokuapp.com/) with flying colors!

## Bugs

- No bugs found

## Updates

### Planned Features

- **Difficulty Levels**: Add different levels of difficulty for computer attacks.
- **Ship Variety**: Implement additional ship types and sizes.
- **Graphical Interface**: Develop a graphical user interface (GUI) for better user experience.
- **Multiplayer Mode**: Enable multiple players to play against each other.

### Recent Changes

- **Input Validation**: Added checks for valid coordinates and preventing re-bombing.
- **Bug Fixes**: Corrected issues with grid display and ship count updates.

## Deployment

### Prerequisites

- Python 3.x must be installed on your system.
- The script should be run in a terminal or command prompt that supports Python.

### Steps to Deploy

1. **Clone the Repository**: 
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```
2. **Run the Game**:
    ```sh
    python battleship.py
    ```

## Other Information

### Code Structure

- **`Battleship` Class**: Contains methods for game setup, playing rounds, displaying grids, and determining the game outcome.
- **`main` Function**: Handles user input for grid size and player name, and initiates the game loop.

### Links

- **Live Link**: [https://bellas-battleship-94168bc0e6f0.herokuapp.com](https://bellas-battleship-94168bc0e6f0.herokuapp.com/)
- **GitHub Link**: [https://github.com/annabellaals/Bellas-Battleship](https://github.com/annabellaals/Bellas-Battleship)

### Credits

- Credits to Code Institude, tasks taught me a lot on how to put things together. Help from mentor, and the slack community.
- Credits to Harvard's Online Courses
- Credits to W3schools.
- Credits to Udemy
- Credits to Code Institute student, helped me on-hand

---

Enjoy playing Bella's Battleship and have fun sinking those ships!