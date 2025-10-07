import random


# Wave 1
VALID_LETTERS = {'R', 'O', 'Y', 'G', 'B', 'P'}

def generate_code():
    code = []
    
    # Generate a code of 4 random letters from VALID_LETTERS
    letters_list = list(VALID_LETTERS)
    return [random.choice(letters_list) for _ in range(4)]

def uppercased_list(char_list):
    """Convert a list of characters to uppercase."""
    uppercased_list = []
    for letter in char_list:
        uppercased_list.append(str(letter).upper())
    return uppercased_list


def validate_guess(guess):
    # Check for empty list or not a list
    if not isinstance(guess, list) or len(guess) != 4:
        return False
    # Check all elements are strings and not None
    for letter in guess:
        if not isinstance(letter, str) or letter is None:
            return False
    # Convert guess to uppercase for case-insensitive comparison
    uppercased_guess = normalize_code(guess)
    # Check all letters are valid
    for letter in uppercased_guess:
        if letter not in VALID_LETTERS:
            return False
    return True

def normalize_code(code):   
    """
    Normalizes the casing for a code by converting 
    the list of characters to uppercase.
    """    
    return [str(letter).upper() for letter in code]

def check_code_guessed(guess, code):
    # Convert guess and code to uppercase for case-insensitive comparison
    uppercased_guess = normalize_code(guess)
    uppercased_code = normalize_code(code)
    # Check if the guess and code are identical (win condition)
    return uppercased_code == uppercased_guess