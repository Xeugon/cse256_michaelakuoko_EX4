# guess_the_word.py
import random

WORD_LIST = ["python", "code", "function", "variable", "syntax", "loop"]

def select_word():
    return random.choice(WORD_LIST)

def play_game():
    word = select_word()
    guessed = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()

    print("Welcome to Guess the Word!")
    
    while attempts > 0 and "_" in guessed:
        print("\nWord:", " ".join(guessed))
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
            for idx, letter in enumerate(word):
                if letter == guess:
                    guessed[idx] = guess
        else:
            attempts -= 1
            print(f"Incorrect! Attempts left: {attempts}")

    if "_" not in guessed:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    play_game()
