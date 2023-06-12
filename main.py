import json
import random

print("Welcome to Hangman's game, good luck & have fun!")
print("*" * 26)
with open("hangman.json", "r") as f:
    json_object = json.loads(f.read())
    life = json_object["life"]
    words = json_object["words"]
    chosen_word = random.choice(words)

display = []

for i in range(len(chosen_word)):
    display += "_"
print(display)
game_over = False
while not game_over:
    guessed_letter = input("Please guess a letter:").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter

    print(display)
    if guessed_letter not in chosen_word:
        life -= 1
        print("The word does not contain the chosen letter")
        if life == 0:
            game_over = True
            print("Game over!")
    if "_" not in display:
        print(f"You won, the guessed word was {chosen_word}.")
        break
