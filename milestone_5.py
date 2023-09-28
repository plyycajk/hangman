import random

class Hangman:

    """Enables the user to play hangman by guessing which letters are contained in a randomly selected word"""

    def __init__(self, word_list, num_lives = 5):
        self.list_of_guesses = []
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.num_letters = len(set(self.word))
        self.word_guessed = [x if x in self.list_of_guesses else '_' for x in self.word]
        
    def check_guess(self, guess):
        self.guess = guess.lower()
        if self.guess in self.word:
            print(f"Good guess {self.guess} is in the word!")
            for count, letter in enumerate(self.word):
                if letter == self.guess:
                    self.word_guessed[count] = self.guess
                else:
                    continue
            self.num_letters = self.num_letters - 1
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {self.guess} is not in the word")
            print(f"You have {self.num_lives} lives left")
    
    def remaining_lives(self):
        return self.num_lives
    
    def remaining_letters(self):
        return self.num_letters
                 
    def ask_for_input(self):
        while True:
            guess = str(input("Please guess a letter"))
            if not guess.isalpha() or len(guess) > 1:
                print("Invalid letter. Please, enter a single alphabetical character")    
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)

#bug "you lost not being triggered on 0 or fewer lives remaining"

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.remaining_lives() == 0:
            print("You lost!")
        elif game.remaining_letters() > 0:
            game.ask_for_input()
            continue
        else:
            print("Congratulations. You won the game!")

play_game(["apple","banana","pear"])