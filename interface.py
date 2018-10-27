import os


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
    print("-------------------- A N A G R A M   S E A R C H E R --------------------")
    print()
    print(" In this game mode, you have to find all the anagrams of the given word. ")
    print()
    print("-------------------------------------------------------------------------")
    print()


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

def anagram_searcher():


def choose_difficulty():
    clear_screen()
    print_title()
    print_difficulty()
    difficulty = input()
    if difficulty == "1":
        difficulty = "EASY"
        return difficulty
    if difficulty == "1":
        difficulty = "NORMAL"
        return difficulty


choose_mode()