
import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"Chosen word is {chosen_word}")
guess = input("Guess a letter: ").lower()

display = []
for letter in chosen_word:
    display += "_"

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)
        