import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:  # FIXED HERE
        word = random.choice(words)
    return word    

def hangman():
    word = get_valid_word(words).upper()  # Ensure uppercase for comparison
    word_letters = set(word)  # Unique letters in the word      
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # Letters guessed by the user

    # Getting the user input
    while len(word_letters) > 0:
        # Letters used
        print("You have used these letters:", ', '.join(used_letters))  # FIXED

        # Current word display
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", ' '.join(word_list))  # FIXED

        user_letter = input("Guess some letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # Correctly removes guessed letter

        elif user_letter in used_letters:
            print("You have already guessed that letter.")

        else:
            print("Invalid character. Try again.")

    print(f"Congratulations! The word was {word}.")  # Message when the game ends

# Run the game
hangman()
