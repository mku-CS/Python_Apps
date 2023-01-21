import sys
import random


# ==== STARTER VARIABLES ====
def generate_word_to_guess():
    lines = open("wordbase.txt").read().splitlines()
    chosenLine = random.choice(lines)
    return chosenLine


number_of_tries = 0
word_to_guess = generate_word_to_guess()
used_letters = []
user_word = []

for _ in word_to_guess:
    user_word.append("_")

# ==== COLORS DEFINITION ====
REGULAR = "\033[39m"
GREEN = "\033[92m"
ORANGE = "\033[93m"
BLINK = "\033[5m"
NOBLINK = "\033[0m"


# ==== FIND INDEXES ====

def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)
    return indexes
# ==== PRINT HANGMAN FUNCTION ====

def print_hangman(tries_left):
    print()
    if tries_left == 0:
        print(f"  ||=====      \n"
              f"  ||/   |      \n"
              f"  ||    {ORANGE}O{REGULAR}      \n"
              f"  ||   {ORANGE}/|\{REGULAR}     \n"
              f"  ||    {ORANGE}|\{REGULAR}     \n"
              f"  ||           \n"
              f"============\n")
        print(f"{ORANGE}U R dead, bro. X[{REGULAR}")
        sys.exit(0)
    elif number_of_tries == 1:
        print("  ||=====       \n"
              "  ||/   |       \n"
              "  ||           \n"
              "  ||        \n"
              "  ||          \n"
              "  ||            \n"
              "============      ")
    elif number_of_tries == 2:
        print("  ||====       \n"
              "  ||          \n"
              "  ||           \n"
              "  ||         \n"
              "  ||          \n"
              "  ||            \n"
              "============      ")
    elif number_of_tries == 3:
        print("  ||       \n"
              "  ||          \n"
              "  ||           \n"
              "  ||         \n"
              "  ||          \n"
              "  ||            \n"
              "============      ")
    elif number_of_tries == 4:
        print("         \n"
              "         \n"
              "             \n"
              "           \n"
              "  ||          \n"
              "  ||            \n"
              "============      ")
    elif number_of_tries == 5:
        print("         \n"
              "         \n"
              "             \n"
              "           \n"
              "            \n"
              "  ||          \n"
              "============      ")
    else:
        print("         \n"
              "         \n"
              "             \n"
              "           \n"
              "            \n"
              "            \n"
              "============      ")

    print()

# ==== SHOW CURRENT STATE OF THE GAME ====

def show_results():
    print(f"\n  {ORANGE}===================================={REGULAR}\n")
    print(f"\t{GREEN}the word to guess: {REGULAR}" + "".join(user_word))
    print(f"\n  {ORANGE}===================================={REGULAR}\n")
    print("Used letters:", used_letters)
    print()
    print_hangman(number_of_tries)
    print()
#    print("Tries left:", number_of_tries)

# ==== LETTER VALIDATION ===+

def letter_validation(letter):
    if len(letter) > 1:
        print("No cheating! only one letter at a time!")
        return
    elif not letter.isalpha():
        print("No cheating! Only letters allowed!")
    elif letter in used_letters:
        print(f"Stop it, you already checked letter {letter}!")
    else:
        return True

# ==== CHOOSE DIFFICULTY FUNCTION ====

def choose_diff():
    print(f"\n{GREEN}Who are you?{REGULAR} (type 1/2/3):\n"
         f"\n {ORANGE}-> 1.{REGULAR} Newborn Baby"
         f"\n {ORANGE}-> 2.{REGULAR} Smart Guy"
         f"\n {ORANGE}-> 3.{REGULAR} Hardcore Player\n")
    while True:
        difficulty = input(f" {ORANGE}==>{REGULAR} ")
        if difficulty == "1":
            tries = 7
            return tries
        elif difficulty == "2":
            tries = 5
            return tries
        elif difficulty == "3":
            tries = 3
            return tries
        else:
            print("Choose 1, 2 or 3")

# ==== INTRO ====
while True:

    print("\n"
          f"{ORANGE}  ||======================================||     \n"
          "  ||/   |      |      |      |      |    \|| \n"
          f"  || {REGULAR}{BLINK}   O      0      O      O      O  {NOBLINK}{ORANGE}   ||   \n"
          f"  ||  {REGULAR}{BLINK} /|\    /|\    /|\    /|\    /|\  {NOBLINK}{ORANGE}  || \n"
          f"  ||  {REGULAR}{BLINK}  |\    /|     /|      |\    /|   {NOBLINK}{ORANGE}  ||\n"
          "  ||                                      ||\n"
          f"  ||======================================||{REGULAR}\n")


    print(f"\tWelcome to {ORANGE}{BLINK}The Hangman{NOBLINK}{REGULAR} game!\n\n\nAre you ready?\n")
    print(f"{GREEN}Y{REGULAR} - let's go!\n{GREEN}N{REGULAR} - get me outta here!!\n")
    startGame = input(f" {ORANGE}==>{REGULAR} ")

    while True:
        if startGame.upper() == "Y":
            number_of_tries = choose_diff()
            print(f"\n\t{GREEN}the word to guess: {REGULAR}" + "".join(user_word))

            break
        elif startGame.upper() == "N":
            print("bye coward!")
            sys.exit(0)
        else:
            print("Choose Y or N!")
            startGame = input(f" {ORANGE}==>{REGULAR} ")

    while True:
#        print(f"\n\t{GREEN}The word to guess{REGULAR}:", "".join(user_word))
        letter = input(f"\nChoose one letter:\n {ORANGE}==>{REGULAR} ")

        if letter_validation(letter):
            used_letters.append(letter)
            found_indexes = find_indexes(word_to_guess, letter)
            if len(found_indexes) == 0:
                print(f"There is no letter {letter} in the word, sorry.")
                number_of_tries -= 1
#                if number_of_tries == 0:
#                    print("U R dead, bro. xx")
#                    sys.exit(0)
#                     while True:
#                         repeat = input("Want to play again? (Y/N\n ==> ")
#                         if repeat.upper() == "Y":
#                             print("to musze zrobic taka funkcje")
#                             #break
#                             sys,exit(0)
#                         elif repeat.upper() =="N":
#                             sys.exit(0)
#                         else:
#                             continue
            else:
                for index in found_indexes:
                    user_word[index] = letter
                if "".join(user_word) == word_to_guess:
                    print(f"\n{GREEN}Congratulations, you are alive!\n{ORANGE}The word is: {REGULAR}{BLINK}", "".join(user_word))
                    print(f"{NOBLINK} ")
                    sys.exit(0)
            show_results()









