# City Battle

City Battle is a shooting game developed in Python using the Pygame library. The goal is to control one or two players to defeat enemies, score points, and survive as long as possible.

## Requirements
- Python 3.10 or higher
- Pygame

## Installation
1. Clone this repository or download the project files.
2. Install the dependencies by running:
   ```sh
   pip install -r requirements.txt
   ```

## How to Play
1. Run the game with:
   ```sh
   python main.py
   ```
2. Choose the game mode in the menu.
3. Use the following controls:

### Player 1
- Move up: **W**
- Move down: **S**
- Move left: **A**
- Move right: **D**
- Shoot: **Left Ctrl**

### Player 2
- Move up: **Up Arrow**
- Move down: **Down Arrow**
- Move left: **Left Arrow**
- Move right: **Right Arrow**
- Shoot: **Right Ctrl**

## Project Structure
- `main.py`: Main file to start the game
- `code/`: Contains all the game source code
- `asset/`: Images and sounds used in the game

## Score and Ranking
The game saves scores in a local SQLite database and displays the ranking of the best players.