import random

word_list = ["satsuma", "plum", "nectarine", "apple", "grapes"]

word = random.choice(word_list)


def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word, try again")
    

def ask_for_input():
    while True:
         guess = input("Please, guess a letter")
         if guess.isalpha() == True and len(guess) == 1:
             check_guess(guess)
             return     
         else:
            print("Invalid letter. Please, enter a single alphabetical character.")
            continue
    


