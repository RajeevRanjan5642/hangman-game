# Author: Rajeev Ranjan
# Date: June 07 2023 08:46 AM

# Hangman Game
# -----------------------------------

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    #opening file in read mode and coppying the content into inFile
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    #converting string into list(of words in string)
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    letters_in_secret_word = list(secret_word)
    
    for i in letters_in_secret_word:
        if i not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    letters_in_secret_word = list(secret_word)
    guessed_word=''
    for i in letters_in_secret_word:
        if i in letters_guessed:
            guessed_word+=i
        else:
            guessed_word+='_ '
    return guessed_word       

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_lowercase_letters = list(string.ascii_lowercase)
    available_letters=''
    for i in all_lowercase_letters:
        if i not in letters_guessed:
            available_letters+=i
    return available_letters

def is_input_valid(letters_guessed,user_input):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    user_input: string, the current character that user has guessed
    returns: bool, if the user has entered either a symbol or a letter that has
             already been guessed return False, True otherwise).
    '''
    if not str.isalpha(user_input):
        print("Oops! That is not a valid letter.")
        return False
    elif user_input in letters_guessed:
        print("Oops! You've already guessed that letter.")
        return False
    else:
        return True
    
def is_match(secret_word,user_input):
    '''
    secret_word: string, the word the user is guessing
    user_input: string, the current letter that user has guessed
    returns: bool, if the letter that user has guessed matches with a letter present 
             in secret word than return True, False otherwise.
    '''
    letters_in_secret_word = list(secret_word)
    if user_input in letters_in_secret_word:
        return True
    else:
        return False

    
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    '''
    
    guesses_left=6
    warnings_available=3
    letters_guessed=[]
    guessed_word=''
    
    while(guesses_left>0):
        
        print("You have",guesses_left,"guesses left.")
        print("Available letters: ",get_available_letters(letters_guessed))
        
        #taking input from user
        user_input = input("Please guess a letter:")
        
        #converting user_input into lowercase
        user_input = str.lower(user_input)
        
        if is_input_valid(letters_guessed, user_input):
            letters_guessed.append(user_input) #add valid input into letters_guessed list
            guessed_word=get_guessed_word(secret_word, letters_guessed)
           
            if is_match(secret_word,user_input):
                print("Good Guess:",guessed_word)
            else:
                if user_input in ['a','e','i','o']: #check whether the input is vowel
                    guesses_left-=2
                else:
                    guesses_left-=1
                    
                print("Oops! That letter is not in my word:",guessed_word)
        else:
            warnings_available-=1
            if warnings_available<0:
                print("You have no warnings left.so you lose one guess:",guessed_word)
                guesses_left-=1
                
            else:
                print("You have",warnings_available,"warnings left:",guessed_word)
        print("----------------------------")
          
        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            unique_letters_in_secret_word=len(set(secret_word))
            score=guesses_left*unique_letters_in_secret_word
            print("Your total score for this game is:",score)
            return
    
    #after while block
    print("Sorry, you ran out of guesses. The word was",secret_word,".")


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    
    
    secret_word = choose_word(wordlist)
    
    print("Welcome to the game Hangman!")
    length_of_secret_word = len(secret_word)
    print("I am thinking of a word that is",length_of_secret_word,"letters long.")
    print("You have 3 warnings left.")
    print("----------------------------")
    
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
    
    