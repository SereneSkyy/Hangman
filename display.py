def show_hangman(wrong_guess):
    """
    Displays the hangman based on the number of wrong guesses.
    """
    stages = [
        """
           -------
           |
           |
           |
           |
           |
        """,
        """
           -------
           |     O
           |
           |
           |
           |
        """,
        """
           -------
           |     O
           |     |
           |
           |
           |
        """,
        """
           -------
           |     O
           |    /|
           |
           |
           |
        """,
        """
           -------
           |     O
           |    /|\\
           |
           |
           |
        """,
        """
           -------
           |     O
           |    /|\\
           |    /
           |
           |
        """,
        """
           -------
           |     O
           |    /|\\
           |    / \\
           |
           |
        """
    ]
    print(stages[wrong_guess])
