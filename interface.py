import os
import sys


def progress(count, total, suffix):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()  # As suggested by Rom Ruben


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_title():
    print(" _     _  _______  ______    ______   _______  ___      _______  __   __")
    print("| | _ | ||       ||    _ |  |      | |       ||   |    |   _   ||  | |  |")
    print("| || || ||   _   ||   | ||  |  _    ||    _  ||   |    |  |_|  ||  |_|  |")
    print("|       ||  | |  ||   |_||_ | | |   ||   |_| ||   |    |       ||       |")
    print("|       ||  |_|  ||    __  || |_|   ||    ___||   |___ |       ||_     _|")
    print("|   _   ||       ||   |  | ||       ||   |    |       ||   _   |  |   |")
    print("|__| |__||_______||___|  |_||______| |___|    |_______||__| |__|  |___| ")
    print()


def print_menu():
    print("-------------- MP LIGHTS BY DIZON, JAMOLANGUE, AND QUIRIM ---------------")
    print()
    print("          1 - START              2 - HELP             3 - QUIT           ")
    print()
    print("-------------------------------------------------------------------------")
    print()


def print_game_modes():
    print("------------------ C H O O S E   A   G A M E   M O D E ------------------")
    print()
    print("            1 - ANAGRAM SEARCHER              2 - WORD FINDER            ")
    print()
    print("-------------------------------------------------------------------------")
    print()


def print_difficulty():
    print("--------------- C H O O S E   T H E   D I F F I C U L T Y ---------------")
    print()
    print("             1 - EASY         2 - NORMAL       3 - DIFFICULT             ")
    print()
    print("-------------------------------------------------------------------------")
    print()


def print_anagram_searcher():
    clear_screen()
    print("-------------------- A N A G R A M   S E A R C H E R --------------------")
    print()
    print(" In this game mode, you have to find all the anagrams of the given word. ")
    print()
    print("-------------------------------------------------------------------------")
    print()


def print_word_finder():
    clear_screen()
    print("------------------------- W O R D   F I N D E R -------------------------")
    print()
    print("      In this game mode, find all possible words from the sequence.      ")
    print()
    print("-------------------------------------------------------------------------")
    print()


def print_game_status_anagram(int_lives, int_words_found, int_score, str_given):
    clear_screen()
    print("-------------------- A N A G R A M   S E A R C H E R --------------------")
    print()
    print("  LIVES :"+str(int_lives)+"               WORDS FOUND: "+str(int_words_found)+"                   SCORE: "+str(int_score))
    print()
    print("-------------------------------------------------------------------------")
    print(" GIVEN WORD: "+str(str_given))
    print("-------------------------------------------------------------------------")


def print_game_status_wordfinder(int_lives, int_words_found, int_score, str_given):
    clear_screen()
    print("------------------------- W O R D   F I N D E R -------------------------")
    print()
    print("  LIVES :"+str(int_lives)+"               WORDS FOUND: "+str(int_words_found)+"                   SCORE: "+str(int_score))
    print()
    print("-------------------------------------------------------------------------")
    print(" GIVEN WORD: "+str(str_given))
    print("-------------------------------------------------------------------------")

def main_menu():
    while True:
        clear_screen()
        print_title()
        print_menu()
        menu = input()
        if menu == "1":
            menu = "START"
            return menu
        elif menu == "2":
            menu = "HELP"
            return menu
        elif menu == "3":
            menu = "QUIT"
            return menu


def choose_mode():
    while True:
        clear_screen()
        print_title()
        print_game_modes()
        mode = input()
        if mode == "1":
            mode = "ANAGRAM SEARCHER"
            return mode
        elif mode == "2":
            mode = "WORD FINDER"
            return mode


def choose_difficulty():
    while True:
        clear_screen()
        print_title()
        print_difficulty()
        difficulty = input()
        if difficulty == "1":
            difficulty = "EASY"
            return difficulty
        elif difficulty == "2":
            difficulty = "NORMAL"
            return difficulty
        elif difficulty == "3":
            difficulty = "DIFFICULT"
            return difficulty
