import random
import os

from hangman_words import word_list
from hangman_art import logo, stages

secret_word = word_list[random.randint(0, len(word_list))]
secret_word_list = []

for i in range (len(secret_word)):
    secret_word_list.append("_")

game_over = False
lives = 6

print(f"{logo} \n")

while game_over == False:

    user_guess = str(input("Guess a letter: ").lower())

    # Clears terminal after each move
    os.system('cls' if os.name == 'nt' else 'clear')

    if user_guess not in secret_word:
        lives = lives - 1
        print(f"You guessed {user_guess.upper()}. That is not a letter.")

        if lives == 0:
            game_over = True
            print(f"You lose! The word was {secret_word.upper()}")

    if user_guess in secret_word_list:
        print("You've already guess that letter.")

    for i in range (len(secret_word)):
        if user_guess == secret_word[i]:
            secret_word_list[i] = user_guess

        if "_" not in secret_word_list:
            game_over = True
            print(f"\nYou win! The word is {secret_word.upper()} \n")
            exit()


    print(stages[lives])
    print(f"\n{' '.join(secret_word_list).upper()}")
    print("\n")