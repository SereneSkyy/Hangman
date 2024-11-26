import display
import logic
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("Welcome to Hangman!")
    word = input("Enter the word for the guesser:").lower()
    print("\n"*50) # Clear the screen to hide the word
    print("The game begins")
    
    guessed_word = ["_" for _ in word]
    max_wrong_guess = 6
    guessed_letters = set()
    wrong_guess = 0
    
    for _ in range(max_wrong_guess +len(word)):
        clear_screen()
    #Display the current state
        print("Word: "+ " ".join(guessed_word))
        display.show_hangman(wrong_guess)
        print(f"Guessed letters: {','.join(sorted(guessed_letters))}")

        #check win condition
        if "_" not in guessed_word:
            print(f"congrats! youve guessed the correct word: {word}")
            break
        
    # get a letter guess
        guess = input("Guess a letter: ").lower()

        if len(guess) !=1 or not guess.isalpha(): 
              # If the guess is more than one character (len(guess) != 1).
              # If the guess contains non-alphabet characters (not guess.isalpha()).
              # So, if either of these conditions is true, the guess is invalid.
            print("Invalid input")
            continue
        
        if guess in guessed_letters:
            print(f"you already guessed '{guess}'. Try another")
            continue

        guessed_letters.add(guess)

        # Check if the guess is in the word

        if guess in word:
            logic.update_guessed_word(word, guessed_word, guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guess +=1
            print(f"Wrong guess !")

        # check lose condition
        if wrong_guess == max_wrong_guess:
            display.show_hangman(wrong_guess)
            print(f"Game Over ! The word was: {word}")
            break
if __name__ == "__main__":
    main()