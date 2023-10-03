import random


class Hangman:
    """
    This class enables the user to play hangman by guessing which letters are contained in a randomly selected word
    
    Attributes:
        word_list (list): the list of words to be guessed from
        num_lives (int): the number of guesses the player has in the game
    """
    def __init__(self, word_list, num_lives = 5):
        self.list_of_guesses = []
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.num_letters = len(set(self.word))
        # creates game board '_' for letters not yet guessed and correctly guessed letters 
        # in the correct place within the word
        self.word_guessed = [x if x in self.list_of_guesses else '_' for x in self.word]
        
    def check_guess(self, guess):
        """
        This function checks whether the letter guessed is in the word
        
        Args:
            guess (str): the letter guessed within the word
        
        Returns:
            str: confirms guess in word or not along with remaining lives 
        """
        self.guess = guess.lower()
        if self.guess in self.word:
            self.num_letters = self.num_letters - 1
            print(f"Good guess {self.guess} is in the word!")
            for count, letter in enumerate(self.word):
                if letter == self.guess:
                    self.word_guessed[count] = self.guess
                else:
                    continue
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {self.guess} is not in the word")
            print(f"You have {self.num_lives} lives left")
                 
    def ask_for_input(self):
            """
            Asks for a guess when playing the hangman game
            
            Returns:
                str: letter guessed if True; otherwise asks for input again
            """
        print(' '.join(self.word_guessed))
        while True:
            guess = str(input("Please guess a letter")).lower()
            if not guess.isalpha() or len(guess) > 1:
                print("Invalid letter. Please, enter a single alphabetical character")    
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess.lower())
                self.check_guess(guess)
                break

def play_game(word_list):
    """
    Runs a game of hangman based word list provided

    Args:
        word_list (list): the list of words from which to guess

    Returns:
        ask_for_input() function if both lives and guesses remain; str win or lose otherwise
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print(f"Congratulations, the word was '{game.word}'. You won the game!")
            break

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
