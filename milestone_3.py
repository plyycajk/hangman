import random

word_list = ["satsuma", "plum", "nectarine", "apple", "grapes"]

word = random.choice(word_list)


def check_guess(letter_guess):
    letter_guess = letter_guess.lower()
    if letter_guess in word:
        print(f"Good guess! {letter_guess} is in the word.")
    else:
        print(f"Sorry, {letter_guess} is not in the word, try again")
    

def ask_for_input():
    while True:
         letter_guess = input("Please, guess a letter")
         if letter_guess.isalpha() == True and len(letter_guess) == 1:
             check_guess(letter_guess)
             return     
         else:
            print("Invalid letter. Please, enter a single alphabetical character.")
            continue
    


