import random
import hangman_art
from hangman_words import word_list

print(hangman_art.logo)
gameOver = False
lives = 6
chosen_word = random.choice(word_list)
# DEBUGGER print(f'Pssst, the solution is {chosen_word}.')
print(hangman_art.stages[6])

guess_database = []

display = []
for letter in chosen_word:
    display.append("_")

while not gameOver:
    guess = input("Guess a letter: ").lower()
    if guess in guess_database:
        print("You have already guessed that letter. Try again.")
    else:
        guess_database.append(guess)
        for n in range(len(chosen_word)):
            if guess == chosen_word[n]:
                display[n] = guess
        if guess not in chosen_word:
            lives -= 1
            print(f"The letter {guess} is not in the word! You lose a life!")
        print(hangman_art.stages[lives])
        print(display)
        if lives == 0:
            print("You have no more lives! You lose!")
            print(f"The word was {chosen_word}")
            gameOver = True
        if "_" not in display:
            print("You win!")
            gameOver = True
