from colorama import Fore, Style
import os
from random import randint
from colorama import init

init()

__author__ = 'Maor Lahat'


def hangman_art():
    """
    this function print the title of the game
    :return: None
    """
    print(Style.BRIGHT)
    print(Fore.YELLOW +
          """
     _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                         __/ |                      
                        |___/
    """)
    print(Style.RESET_ALL, end="")


# ----------
def print_hangman(num_of_tries):
    """
    This function prints the position of the hang man
    :param num_of_tries: Literally
    :return: None
    """
    HANGMAN_PHOTOS = {}
    HANGMAN_PHOTOS[1] = """
    x-------x
    
    
    
    
    
    """
    HANGMAN_PHOTOS[2] = """
    x-------x
    |
    |
    |
    |
    |
    """
    HANGMAN_PHOTOS[3] = """
    x-------x
    |       |
    |       0
    |
    |
    |
    """
    HANGMAN_PHOTOS[4] = """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """
    HANGMAN_PHOTOS[5] = """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """
    HANGMAN_PHOTOS[6] = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """
    HANGMAN_PHOTOS[7] = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """
    print(Fore.YELLOW + HANGMAN_PHOTOS[int(num_of_tries)])
    print(Style.RESET_ALL, end="")

    # ----------
    """
    This function contains in a dictionary all the vocabulary of the various topics that are in txt files
    :param subjects: the dictionary
    :type subjects: dict
    :return: the dictionary
    :rtype: dict
    """


def dictionary_of_subjects():
    subjects = {}
    subjects[1] = ["Animals", r"c:\users\public\Animals.txt"]
    subjects[2] = ["Countries", r"c:\users\public\Countries.txt"]
    subjects[3] = ["Food", r"c:\users\public\Food.txt"]

    return subjects


# ----------
def print_subject(subject):
    """
     This function get a string and print it with design, its purpose is to print the chosen theme of the word
     :param subject: the theme
     :type subject: string
     :return: None
     """
    print(Style.BRIGHT)
    print(Fore.YELLOW + "    " + subject)
    print(Style.RESET_ALL, end="")

    # ----------
    """
    This function randomly selects a subject from the dictionary
    :param dictionary_of_subjects: dictionary of subjects
    :param dict_keys: all the keys in the dictionary
    :param num_of_subjects: the number of subjects in the dictionary
    :param legal_index: the index after deviation if any
    :param subject: the selected subject
    :type dictionary_of_subjects: dict
    :type dict_keys: list
    :type num_of_subjects: int
    :type legal_index: int
    :type subject: list
    :return: the dictionary
    :rtype: dict
    """


def choose_subject(dictionary_of_subjects):
    dict_keys = dictionary_of_subjects.keys()
    num_of_subjects = len(dict_keys)
    index = randint(1, 10000)
    legal_index = (int(index) % int(num_of_subjects)) + 1
    subject = dictionary_of_subjects[legal_index]
    return subject


# ----------

def choose_word_auxiliary(subject, index):
    """
    this function take a word from a file text
    :param subject: a list with the subject and the file path
    :param index: a number that point on the word in the place of the index
    :type subject: list
    :type index: int
    :return: the word that the index point on, in the file text
    :rtype: str
    """
    file_path = subject[1]
    f_open = open(file_path, "r")
    words_file_lines = f_open.readlines()

    list_of_all_words = []
    # Splits all the lines into words and puts it all in one list
    for line in words_file_lines:
        temporary_list = line.split()
        for words_of_line in temporary_list:
            list_of_all_words.append(words_of_line)

    the_number_of_words = len(list_of_all_words)

    legal_index = int(index) % int(
        the_number_of_words)  # If the index exceeds the number of words then it brings the remainder

    secret_word_by_index = list_of_all_words[legal_index - 1]

    temporary_list = []
    the_number_of_words_without_duplicates = 0  # zero it's a temporary number until we will count the amounts of words
    # counts the words in the list without duplicates, by putting all the words that already benn count in a list
    # and check the next word if it is in the list (the list that save the words that been count)
    for word in list_of_all_words:
        if word not in temporary_list:
            the_number_of_words_without_duplicates += 1
            temporary_list.append(word)
    tup = (subject[0], secret_word_by_index)
    return tup


# ----------
def choose_word():
    index = randint(1, 10000)
    subject = choose_subject((dictionary_of_subjects()))
    return choose_word_auxiliary(subject, index)


# ----------
def show_hidden_word(secret_word, old_letters_guessed):
    """
    this function shows the user the letters in the secret word that been guessed currently
    :param secret_word: the word that the user need to find
    :param old_letters_guessed: a list with all the guesses that the player guessed before
    secret word
    :type secret_word: string
    :type old_letters_guessed: list
    :return: a string with the letters that been guess currently, arranged in the same location like the secret word
    :rtype: String
    """
    whats_found = ""
    in_word = False
    for letter_from_guess in secret_word:  # passes over the letters in the secret word
        for in_list in old_letters_guessed:  # passes over the elements (the letters) in the list of the letters that
            if letter_from_guess == in_list:  # been guessed
                in_word = True
        if in_word:
            whats_found += letter_from_guess
        else:
            whats_found += "_"
        in_word = False
    separator = ' '
    return """
    
    
    """ + separator.join(whats_found)


# ----------
def check_valid_input(letter_guessed, old_letters_guessed):
    """
    this function checks if the guess is valid input
    :param letter_guessed: the player's guess
    :param old_letters_guessed: a list with all the guesses that the player guessed before
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: True if the input is valid and wasn't guessed before and false otherwise
    :rtype: boolean
    """
    lowercase_letter_guessed = letter_guessed.lower()  # change the letter that was guessed to lower case
    letter_guessed_length = len(lowercase_letter_guessed)  # save the length of the letter that was guessed
    # check if the guess is one char and is one of the alphabet and if the user didn't guess it before
    if ((letter_guessed_length > 1) or (not lowercase_letter_guessed.isalpha())
            or (lowercase_letter_guessed in old_letters_guessed)):
        return False
    else:
        return True


# ----------
def try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word):
    """
    this function append the letter that was guessed to the list if it's a valid guess and return True
    otherwise the function print X and the list (sorted) and return False
    :param secret_word: Literally
    :param letter_guessed: the player's guess
    :param old_letters_guessed: a list with all the guesses that the player guessed before
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: True if the input is valid and wasn't guessed before and false otherwise
    :rtype: boolean
    """
    # check if the guess is one char and is one of the alphabet and if the user didn't guess it before
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())  # append the letter that was guessed to the list of the
        return True  # letters that the user guessed before
    else:
        print(Fore.GREEN + show_hidden_word(secret_word, old_letters_guessed))
        print(Style.RESET_ALL, end="")
        print(Style.BRIGHT)
        print(Fore.RED + """   
         X               """)
        old_letters_guessed.sort()
        separator = ' -> '
        print(Fore.RED + separator.join(old_letters_guessed))
        print(Style.RESET_ALL, end="")
        return False


# ----------
def check_win(secret_word, old_letters_guessed):
    """
    this function checks if the player succeeded to guess all the letters in the secret word
    :param secret_word: the word that the user need to find
    :param old_letters_guessed: a list with all the guesses that the player guessed before
    :type secret_word: string
    :type old_letters_guessed: list
    :return: True if the player won and succeeded to guess the secret word, False otherwise
    :rtype: boolean
    """
    match = False
    final_match = True
    for letter_word in secret_word:  # passes over the letters in the secret word
        for letter_list in old_letters_guessed:  # passes over the elements (the letters) in the list of the letters
            # that been guessed
            if letter_word == letter_list:
                match = True
        if not match:
            final_match = False
            break
        match = False
    return final_match


# ------------------------------------------

def main():
    os.system('cls')

    # Setting Variables
    subject = choose_word()
    secret_word = subject[1]
    sub_title = subject[0]
    num_of_tries = 1
    MAX_TRIES = 7  # The max tries plus one
    old_letters_guessed = []
    win = False

    hangman_art()
    print_subject(sub_title)
    print(Style.BRIGHT)
    print("\nLet's Start, Good Luck!")
    print(Style.RESET_ALL, end="")
    print_hangman(num_of_tries)
    print(Fore.GREEN + show_hidden_word(secret_word, old_letters_guessed))
    print(Style.RESET_ALL, end="")

    while num_of_tries != MAX_TRIES and not win:
        letter_guessed = input("Guess a letter:   ")
        os.system('cls')
        hangman_art()
        print_subject(sub_title)
        print_hangman(num_of_tries)
        letter_guessed = letter_guessed.lower()
        if try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word):
            if letter_guessed in secret_word:
                print(Fore.GREEN + show_hidden_word(secret_word, old_letters_guessed))
                print(Style.RESET_ALL, end="")
            else:
                num_of_tries += 1
                os.system('cls')
                hangman_art()
                print_subject(sub_title)
                print_hangman(num_of_tries)
                print(Fore.GREEN + show_hidden_word(secret_word, old_letters_guessed))
                print(Style.RESET_ALL, end="")
        if num_of_tries == MAX_TRIES:
            print(Style.BRIGHT)
            print(Fore.RED + "LOSE")
            print(Fore.RED + "The word was: " + secret_word)
            print(Style.RESET_ALL, end="")
        if check_win(secret_word, old_letters_guessed):
            print(Style.BRIGHT)
            print(Fore.GREEN + "WIN")
            print(Style.RESET_ALL, end="")
            win = True


if __name__ == "__main__":
    main()
