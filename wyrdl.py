# wyrdl.py

import os
import pathlib
import random
from string import ascii_letters

from rich.console import Console
from rich.panel import Panel
from rich.theme import Theme

# Get terminal width and calculate spacing
terminal_width = os.get_terminal_size().columns
letter_spacing = "   " if terminal_width > 100 else "  " if terminal_width > 80 else " "

console = Console(theme=Theme({"warning": "red on yellow"}))

def main():
    # Pre-process
    words_path = pathlib.Path(__file__).parent / "wordlist.txt"
    word_list = words_path.read_text(encoding="utf-8").split("\n")
    word = get_random_word(word_list)
    valid_words = set(w.upper().strip() for w in word_list if len(w.strip()) == 5 and all(letter in ascii_letters for letter in w.strip()))
    guesses = ["_" * 5] * 6  # Keep as single underscores

    # Process (main loop)
    for idx in range(6):
        while True:
            refresh_page(headline=f"Guess {idx + 1}")
            show_guesses(guesses, word)

            guess = input("\nGuess word: ").upper().strip()
            
            if len(guess) != 5:
                console.print("[bold red]Please enter a 5-letter word.[/]")
                input("Press Enter to continue...")
                continue
            elif guess not in valid_words:
                console.print(f"[bold red]'{guess}' is not a valid word. Try again.[/]")
                input("Press Enter to continue...")
                continue
            else:
                guesses[idx] = guess
                break
                
        if guesses[idx] == word:
            break

    # Post-process
    game_over(guesses, word, guessed_correctly=guesses[idx] == word)

def refresh_page(headline):
    console.clear()
    # We'll handle the panel in show_guesses now - just store the headline
    global current_headline
    current_headline = headline

def get_random_word(word_list):
    words = [
        word.upper()
        for word in word_list
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]
    return random.choice(words)

def show_guesses(guesses, word):
    # Build all the guess lines first
    guess_lines = []
    for guess in guesses:
        styled_guess = []
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = "bold black on green"  # Changed to black text
            elif letter in word:
                style = "bold black on yellow"  # Changed to black text
            elif letter in ascii_letters:
                style = "bold white on #666666"  # Keep white on gray
            else:
                style = "dim"
            
            # Make all characters the same size with padding
            if letter == "_":
                display_char = "___"  # Longer underscores
            else:
                display_char = f"_{letter}_"  # Add underscores around letters to match width
            styled_guess.append(f"[{style}]{display_char}[/]")

        guess_lines.append(letter_spacing.join(styled_guess))
    
    # Combine headline and guess content in one panel with title in border
    combined_content = f"[bold blue]{current_headline}[/]\n\n" + "\n".join(guess_lines)
    panel = Panel(combined_content, title="✨ Wyrdle ✨", style="bright_white", padding=(1, 2))
    console.print(panel, justify="center")

def game_over(guesses, word, guessed_correctly):
    refresh_page(headline="Game Over")
    show_guesses(guesses, word)

    if guessed_correctly:
        console.print(f"\n[bold black on green]Correct, the word is {word}[/]")
    else:
        console.print(f"\n[bold white on red]Sorry, the word was {word}[/]")

if __name__ == "__main__":
    main()