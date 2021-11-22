# Problem Set 2, hangman.py
# Name: Anton
# Collaborators:
# Time spent: 

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
from os import makedirs
import random
import string

WORDLIST_FILENAME = "words.txt"

    


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()



def is_word_guessed(secret_word, letters_guessed):
    list_of_secwor = list(secret_word)
    stri = ''
    for i in list_of_secwor:
      if i in letters_guessed:
        stri = stri + i
      else:
        stri = stri + '_ '
    return stri



def get_guessed_word(secret_word, letters_guessed):
    list_of_secwor = list(secret_word)
    for i in list_of_secwor:
      if i in letters_guessed:
        continue
      else:
        return False
    return True



def get_available_letters(letters_guessed):
    list_of_all = list(string.ascii_lowercase)
    for i in letters_guessed:
      if i in list_of_all:
        list_of_all.remove(i)
    stri = ''
    for i in list_of_all:
      stri = stri + i
    return stri
    
    

def hangman(secret_word):
    num_of_guesses = 6
    num_of_warnings = 3
    print('You have', num_of_warnings, 'warnings left')
    list_of_let = []
    while True:
      print('-'*15)
      if num_of_guesses <= 0:
        print('Sorry, you ran out of guesses. The word was "', secret_word, '"')
        break
      print('You have', num_of_guesses, 'guesses left')
      print('Available letters:', get_available_letters(list_of_let))
      let = input('Please guess a letter:').lower()
      if (not let.isalpha()):
        print('Ooops! Enter the letter.')
        if num_of_warnings == 0:
          num_of_guesses = num_of_guesses - 1
        else:
          num_of_warnings = num_of_warnings - 1
          print('You have', num_of_warnings, 'warnings left')
      elif len(list(let)) != 1:
        print('Ooops! Enter one letter!')
        if num_of_warnings == 0:
          num_of_guesses = num_of_guesses - 1
        else:
          num_of_warnings = num_of_warnings - 1
          print('You have', num_of_warnings, 'warnings left')
      elif (not let in list(get_available_letters(list_of_let))):
        print('Ooops! You have already entered this letter!')
        if num_of_warnings == 0:
          num_of_guesses = num_of_guesses - 1
        else:
          num_of_warnings = num_of_warnings - 1
          print('You have', num_of_warnings, 'warnings left')
      else:
        list_of_let.append(let)
        if let in list(secret_word):
          print('Good guess:', is_word_guessed(secret_word, list_of_let))
        elif not let in list(secret_word) and let in ['a', 'e', 'i', 'o', 'u']:
          print('Oops! That letter is not in my word.')
          num_of_guesses = num_of_guesses - 2
          print('Please guess a letter:', is_word_guessed(secret_word, list_of_let))
        elif not let in list(secret_word):
          print('Oops! That letter is not in my word.')
          num_of_guesses = num_of_guesses - 1
          print('Please guess a letter:', is_word_guessed(secret_word, list_of_let))
        if get_guessed_word(secret_word, list_of_let) == True:
          print('-'*15)
          uniqe_let = []
          for i in list(secret_word):
            if i in uniqe_let:
              continue
            else:
              uniqe_let.append(i)
          total_score = num_of_guesses*len(uniqe_let)
          print('Congratulations, you won! \nYour total score for this game is:', total_score)
          break




def match_with_gaps(my_word = 'a_ ple', other_word = 'aople' ):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word_list = list(my_word.replace(" ", ""))
    other_word_list = list(other_word)
    let_list = []
    for i in my_word_list:
      if i != '_':
        let_list.append(i)
    if len(my_word_list) == len(other_word_list):
      for i in range(len(my_word_list)):
        if my_word_list[i] == other_word_list[i]:
          continue
        if my_word_list[i] == '_' and other_word_list[i] in let_list:
          return False
        elif my_word_list[i] != other_word[i] and my_word_list[i] != '_':
          return False
      else:
        return True
    else:
      return False





def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    flag = 0
    for i in wordlist:
      if match_with_gaps(my_word, i):
        flag = 1
        print(i)
    if(flag == 0): print("No matches found")



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
    num_of_guesses = 6
    num_of_warnings = 3
    print('You have', num_of_warnings, 'warnings left')
    list_of_let = []
    while True:
      print('-'*15)
      if num_of_guesses <= 0:
        print('Sorry, you ran out of guesses. The word was "', secret_word, '"')
        break
      print('You have', num_of_guesses, 'guesses left')
      print('Available letters:', get_available_letters(list_of_let))
      let = input('Please guess a letter: ').lower()
      if (let != '*' and not let.isalpha()):
        print('Ooops! Enter the letter.')
        if num_of_warnings == 0:
          num_of_guesses = num_of_guesses - 1
        else:
          num_of_warnings = num_of_warnings - 1
          print('You have', num_of_warnings, 'warnings left')
      elif len(list(let)) != 1:
        print('Ooops! Enter one letter!')
        if num_of_warnings == 0:
          num_of_guesses = num_of_guesses - 1
        else:
          num_of_warnings = num_of_warnings - 1
          print('You have', num_of_warnings, 'warnings left')
      elif (not let in list(get_available_letters(list_of_let)) and let != '*'):
        print('Ooops! You have already entered this letter!')
        if num_of_warnings == 0:
          num_of_guesses = num_of_guesses - 1
        else:
          num_of_warnings = num_of_warnings - 1
          print('You have', num_of_warnings, 'warnings left')
      else:
        if let == '*':
          show_possible_matches(is_word_guessed(secret_word, list_of_let))
          continue
        list_of_let.append(let)
        if let in list(secret_word):
          print('Good guess:', is_word_guessed(secret_word, list_of_let))
        elif not let in list(secret_word) and let in ['a', 'e', 'i', 'o', 'u']:
          print('Oops! That letter is not in my word.')
          num_of_guesses = num_of_guesses - 2
          print('Please guess a letter:', is_word_guessed(secret_word, list_of_let))
        elif not let in list(secret_word):
          print('Oops! That letter is not in my word.')
          num_of_guesses = num_of_guesses - 1
          print('Please guess a letter:', is_word_guessed(secret_word, list_of_let))
        if get_guessed_word(secret_word, list_of_let) == True:
          print('-'*15)
          uniqe_let = []
          for i in list(secret_word):
            if i in uniqe_let:
              continue
            else:
              uniqe_let.append(i)
          total_score = num_of_guesses*len(uniqe_let)
          print('Congratulations, you won! \nYour total score for this game is:', total_score)
          break
    




if __name__ == "__main__":
    print(match_with_gaps())
    


    #secret_word = choose_word(wordlist)
    
    #hangman(secret_word)

    
    secret_word = choose_word(wordlist)
    print('Welcome to the game Hangman!\nI am thinking of a word that is', len(list(secret_word)), 'long.')
    hangman_with_hints(secret_word)
    
