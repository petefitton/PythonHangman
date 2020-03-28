test = "m o u n t a i n"

# applies to every letter but first and last, more or less
test = test[0:1 + 1] + "a" + test[2 + 1:]

# first letter case: index is zero
test2 = "f" + test[1:]

# last letter case: index is the length of string minus one
test3 = test[:-1] + "m"
# test[0] = "f"

print(test)
print(test2)
print(test3)

hangman = """______
|    |
|    O
|   /|\\
|   / \\
|_________"""

print(hangman)

hangman2 = "______"
hangman3 = "|    |"
hangman4 = "|    O"
hangman5 = "|   /|\\"
hangman6 = "|   / \\"
hangman7 = "|__________"

print(hangman2 + "\n" + hangman3 + "\n" + hangman4 + "\n" + hangman5 + "\n" + hangman6 + "\n" + hangman7)