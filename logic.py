def update_guessed_word(word, guessed_word, guess):
    """
    Updates the guessed_word list with the guessed letter at the correct positions.
    """
    for i, letter in enumerate(word):
        if letter == guess:
            guessed_word[i] = guess
