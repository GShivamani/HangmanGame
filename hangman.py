"""
CodeAlpha Python Internship - Task 1: Hangman Game
Concepts used: random, while loop, if-else, strings, lists
"""

import random

# Small list of 5 predefined words (no file or API needed)
WORDS = ["python", "internship", "program", "keyboard", "developer"]
MAX_WRONG_GUESSES = 6


def choose_word():
    """Pick a random word from the predefined list."""
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    """Return the word with unguessed letters shown as underscores."""
    shown = []
    for letter in word:
        if letter in guessed_letters:
            shown.append(letter)
        else:
            shown.append("_")
    return " ".join(shown)


def play_game():
    word = choose_word()
    guessed_letters = []   # every letter the player has tried
    wrong_guesses = 0

    print("\n=== HANGMAN ===")
    print(f"Guess the word one letter at a time. You may miss {MAX_WRONG_GUESSES} times.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("Word:", display_word(word, guessed_letters))
        print(f"Wrong guesses left: {MAX_WRONG_GUESSES - wrong_guesses}")
        print("Guessed so far:", " ".join(guessed_letters) if guessed_letters else "-")

        guess = input("Enter a letter: ").strip().lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).\n")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess!\n")

        # Win check: every letter of the word has been guessed
        if all(letter in guessed_letters for letter in word):
            print("Word:", display_word(word, guessed_letters))
            print(f"Congratulations! You guessed the word '{word}'!")
            return

    print(f"Game over! You ran out of guesses. The word was '{word}'.")


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
