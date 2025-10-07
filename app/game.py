import random


# Wave 1
VALID_LETTERS = {'R', 'O', 'Y', 'G', 'B', 'P'}

def generate_code():
    code = []
    
    # Generate a code of 4 random letters from VALID_LETTERS
    for _ in range(4):
        code.append(random.choice(list(VALID_LETTERS)))

    return code


def validate_guess(guess):
    # Exit early if guess is not exactly 4 elements long
    if len(guess) != 4:
        return False
    
    # Convert guess to uppercase for case-insensitive comparison
    uppercased_guess = []
    for letter in guess:
        uppercased_guess.append(str(letter).upper())

    # Return False if we find an invalid element of guess
    for letter in uppercased_guess:
        if letter not in VALID_LETTERS:
            return False
        
    return True


def check_code_guessed(guess, code):
    # Convert guess to uppercase for case-insensitive comparison
    uppercased_guess = []
    for letter in guess:
        uppercased_guess.append(str(letter).upper())

    # Check if the guess and code are identical (win condition)
    # The guard clause guarantees the number of guesses is 8 or less
    return code == uppercased_guess