# 🪨📄✂️ Rock, Paper, Scissors - Python Terminal Game

A classic Rock, Paper, Scissors game built in Python, playable directly in the terminal. This project marks a step in my Python learning journey, focusing on control flow, user input validation, and implementing basic game logic.

## 🚀 Overview
This script allows a user to play Rock, Paper, Scissors against a computerized opponent. It features custom ASCII art for a fun visual experience in the console and includes robust error handling to prevent the game from crashing if the user types something unexpected.

## ✨ Features
* **Interactive Gameplay:** Play against the computer, whose choices are generated randomly.
* **Input Validation:** Uses `try/except` blocks to catch exceptions, ensuring the user inputs a valid number (0, 1, or 2).
* **Terminal Graphics:** Uses multiline strings to display fun ASCII art for each choice.
* **Infinite Play:** The game loops seamlessly so players can play as many rounds as they want without restarting the program.

## 💻 How to Run
To play the game on your local machine, follow these steps:

1. **Ensure you have Python installed.** You can download it from [python.org](https://www.python.org/).
2. **Clone this repository:**
   ```bash
   git clone https://github.com/windycodin/rock-paper-scissors-python.git
   ```
3. **Navigate to the directory:**
```bash
cd rock-paper-scissors-python 
```
4. **Run the script:**
   ```bash
   python rockpaperscissors.py
   ```


## 🧠 Lessons Learned
Building this project helped me solidify several core Python concepts:

* Handling user inputs securely without breaking the program.

* Utilizing the random module to create unpredictable computer behavior.

* Using lists and index mapping to connect a user's integer choice to a specific visual output (the ASCII art).

* Structuring complex if/elif statements to determine win/loss/draw states.
