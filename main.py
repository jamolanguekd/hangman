import interface
import engine
import random

dictionary = engine.load_dictionary("dictionary_sample.txt")
menu = interface.main_menu()
mode = ""
difficulty =""

lives = 0

while menu != "QUIT":

    if menu == "START":
        mode = interface.choose_mode()
        if mode == "ANAGRAM SEARCHER":

            difficulty = interface.choose_difficulty()

            anagram_list = []
            while len(anagram_list) <= 1:
                given = random.choice(dictionary)
                anagram_list = engine.anagram_searcher(given, dictionary)

            lives = 0
            score = 0
            words_found = 0

            if difficulty == "EASY":
                lives = 5
            elif difficulty == "NORMAL":
                lives = 3
            elif difficulty == "DIFFICULT":
                lives = 1

            interface.print_anagram_searcher()

            while lives > 0 and len(anagram_list) > 0:
                interface.print_game_status(lives, words_found, score, given)
                word = str(input()).lower()
                if engine.word_checker(given, word, anagram_list):
                    score += engine.compute_score(word)
                    words_found +=1
                    anagram_list.remove(word)
                    interface.print_game_status(lives,words_found,score,given)
                else:
                    lives -= 1
                    interface.print_game_status(lives, words_found, score, given)

            if lives == 0:
                interface.clear_screen()
                print("YOU LOSE")
                input()
            else:
                interface.clear_screen()
                print("YOU WIN")
                input()
            menu = interface.main_menu()

        elif mode == "WORD FINDER":


exit()
