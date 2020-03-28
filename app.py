from random import random
from math import floor

# Initialize game
secret_words = ["development", "random", "postman", "mountain", "python", "wrong"]
random_index = floor(random() * 6)
secret_word = secret_words[random_index]
letters_left = len(secret_word)
hangman_guesses_left = 6
letters_guessed = []

hangman2 = "______"
hangman3 = "|    |"
hangman4 = "|    O"
hangman5 = "|   /|\\"
hangman6 = "|   / \\"
hangman7 = "|__________"

print(secret_word) #For use testing

underscored_secret_word = ""
for letter in secret_word:
  underscored_secret_word = underscored_secret_word + "_ "


# Function Definitions
def lose():
  print("HANGMAN. :(")
  print(f"The word was {secret_word}.")

def win():
  print("You won!")
  print(f"The word was {secret_word}.")

def add_to_guesses(guess):
  letters_guessed.append(guess)

def success(guess):
  global underscored_secret_word
  global win
  print("Correct")
  add_to_guesses(guess)
  index = 0
  for letter in secret_word:
    if letter == guess:
      if index == 0:
        underscored_secret_word = guess + underscored_secret_word[1:]
      elif index < (len(secret_word) - 1):
        underscored_secret_word = underscored_secret_word[0:((index * 2))] + guess + " " + underscored_secret_word[(index * 2 + 2):]
      else:
        underscored_secret_word = underscored_secret_word[:-2] + guess
    index += 1
  # if all letters guessed, then run win()
  i = 0
  for letter in underscored_secret_word:
    if letter == "_":
      game_loop()
      return
    if i == (len(underscored_secret_word) - 1) and letter != "_":
      win()
      return
    i += 1

hangman_table = [
  f'\n{hangman2}\n{hangman3}\n{hangman4}\n{hangman5}\n{hangman6}\n{hangman7}\n',
  f'\n{hangman3}\n{hangman4}\n{hangman5}\n{hangman6}\n{hangman7}\n',
  f'\n{hangman4}\n{hangman5}\n{hangman6}\n{hangman7}\n',
  f'\n{hangman5}\n{hangman6}\n{hangman7}\n',
  f'\n{hangman6}\n{hangman7}\n',
  f'\n{hangman7}\n'
]

def hangman(left):
  # print hangman
  global hangman_table
  print(hangman_table[left])

def failure(guess):
  global hangman_guesses_left
  add_to_guesses(guess)
  hangman_guesses_left -= 1
  hangman(hangman_guesses_left)
  game_loop()


# Game Loop
def game_loop():
  print(f"You have {hangman_guesses_left} guesses left.")
  print(f"You have guessed: {letters_guessed}")
  print(f"The word you need: {underscored_secret_word}")

  if hangman_guesses_left > 0:
    guess = input("Guess a letter:\n")
    # Edge cases for guessing more than one letter or non-letter chars
    for letter in secret_word:
      if letter == guess:
        success(guess)
        return
      else:
        continue
    failure(guess)
    return
  if hangman_guesses_left <= 0:
    lose()

game_loop()