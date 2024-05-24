# sudoku-game-with-sudoku-solver in Python

## Overview

This project is a comprehensive Sudoku game built with Python, featuring a graphical interface using pygame and an integrated Sudoku solver using the backtracking algorithm. The game allows users to play Sudoku with different difficulty levels and provides an option to solve any given Sudoku puzzle.

## Features

- **Interactive Sudoku Game**:
  - Play Sudoku with a graphical interface.
  - Select difficulty levels (easy, medium, hard).
  - User-friendly interface with pygame library for graphics.
  - Validate moves and provide feedback.

- **Sudoku Solver**:
  - Solve any valid Sudoku puzzle using the backtracking algorithm.
  - Input custom puzzles and get instant solutions.

## Technologies Used

- **Programming Language**: Python
- **Graphics**: pygame library for GUI
- **Algorithm**: Backtracking algorithm for Sudoku solver

## Usage

1. **Run the Game**:
    - Execute the main script to start the game:
    ```bash
    python main.py
    ```

2. **Game Instructions**:
    - Select a difficulty level to start a new game.
    - Click on a cell and enter a number (1-9) to make a move.
    - Use the solver feature to solve the current puzzle or input a custom puzzle to see the solution.

3. **Sudoku Solver**:
    - Input a custom puzzle through the graphical interface.
    - Click the "Solve" button to visualize the solving process.

## How It Works

- **Sudoku Game**: The game generates puzzles of varying difficulty. The user interacts with the puzzle through a pygame library for graphics interface, making moves and receiving real-time validation.
- **Sudoku Solver**: The solver uses a backtracking algorithm to find the solution to any valid Sudoku puzzle. It recursively fills empty cells while ensuring no conflicts with Sudoku rules, backtracking when necessary.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## Contact

For any inquiries or support, please contact vishal.dsai22@iitg.ac.in .

---

Enjoy solving and playing Sudoku with this interactive Python application!
