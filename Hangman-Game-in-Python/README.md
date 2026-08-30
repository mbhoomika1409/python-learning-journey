Hangman Game in Python

Hangman is a classic word-guessing game. Its origins are not exactly known but it appears 
to date back to Victorian times. A player writes down the first and last letters of a word 
and another player guesses the letters in between.

Program randomly selects a word from a list of secret words.
Player has limited chances to guess the word.
When a correct letter is guessed, it is revealed in its correct position.
Player wins if all letters are guessed before running out of chances.

# Steps to Build the Game

Create a list of words and randomly select one.
Display blanks (_) for each letter in the word.
Take a letter as input from the user.
Check whether the letter exists in the word.
Reveal correct letters and track wrong guesses.
Display the Hangman drawing after each incorrect guess.
End the game when the word is guessed or all chances are used.

#code

import random

words = ["apple", "banana", "mango", "orange", "grapes", "papaya"]

word = random.choice(words)
guessed = []
wrong_guesses = 0
max_attempts = 6

hangman = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

print("Welcome to Hangman!")
print("Hint: The word is a fruit.")

while wrong_guesses < max_attempts:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print(hangman[wrong_guesses])
    print("Word:", display)

    if "_" not in display:
        print("Congratulations! You won!")
        print("The fruit was:", word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print(hangman[wrong_guesses])
    print("Game Over!")
    print("The fruit was:", word)




Explanation:

words contains different fruit names.
random.choice() randomly selects one fruit.
print() displays the hint: "The word is a fruit."
guessed stores the letters entered by the player.
hangman contains the different stages of the Hangman drawing.
while loop continues the game until the player wins or loses.
Correct guesses reveal letters; wrong guesses update the Hangman drawing.
The player wins when all letters are guessed.
The game ends after 6 wrong guesses.


Output:-

Welcome to Hangman!
Hint: The word is a fruit.

     -----
     |   |
         |
         |
         |
    =========
    
Word: _ _ _ _ _ _ 
Guess a letter: b
Correct guess!

     -----
     |   |
         |
         |
         |
    =========
    
Word: b _ _ _ _ _ 
Guess a letter: a
Correct guess!

     -----
     |   |
         |
         |
         |
    =========
    
Word: b a _ a _ a 
Guess a letter: n
Correct guess!

     -----
     |   |
         |
         |
         |
    =========
    
Word: b a n a n a 
Congratulations! You won!
The fruit was: banana
