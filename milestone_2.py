import random

word_list = ["satsuma", "plum", "nectarine", "apple", "grapes"]

word = random.choice(word_list)

guess = input("Please enter one letter")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops, that's not a valid input")

