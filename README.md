#  Python Wyrdl

A word-guessing game inspired by Wordle, built with Python and Rich, that runs in the terminal based on [Real Python's tutorial](https://realpython.com/python-wordle-clone/)

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/elspear/wyrdle.git
   cd wyrdle
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## How to Play

Run the game with:
```bash
python wyrdl.py
```

- You have 6 attempts to guess a 5-letter word
- Letters are color-coded:
  - **Green**: Correct letter in the correct position
  - **Yellow**: Correct letter in the wrong position  
  - **Gray**: Letter not in the word
- Type your guess and press Enter

## Current features

- Classic Wordle mechanics 
- 5 letter word guessing, letters display in green, yellow, or gray
- Word list of 10,000 most used words
- All guesses are checked against the english dictionary
- Enhanced visual display with larger letter formatting

## Future features

- Expand on rich formatting to make the game more visually appealing 
- Variable word length where the input is adjusted dynamically

## Requirements

- Python 3.7+
- Rich library

## 
