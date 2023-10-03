import random

word_list = ["satsuma", "plum", "nectarine", "apple", "grapes"]

word = random.choice(word_list)


def check_guess(letter_guess):
    #check whether letter guessed exists within selected word and informs user
    letter_guess = letter_guess.lower()
    if letter_guess in word:
        print(f"Good guess! {letter_guess} is in the word.")
    else:
        print(f"Sorry, {letter_guess} is not in the word, try again")
    

def ask_for_input():
    #asks for guess from user, checks if input is a single alphabetical character before calling check_guess function
    letter_guess = input("Please, guess a letter")
    while letter_guess.isalpha() == False or len(letter_guess) > 1:
        print("Invalid letter. Please, enter a single alphabetical character.")
        letter_guess = input("Please, guess a letter")
    else:
        check_guess(letter_guess)


    
    