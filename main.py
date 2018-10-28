import interface
import engine
import random


dictionary = engine.load_dictionary("dictionary.txt")
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
            invalid_list = []
            while len(anagram_list) <= 10:
                given = random.choice(dictionary)
                if given not in invalid_list:
                    invalid_list.append(invalid_list)
                else:
                    continue
                anagram_list = engine.anagram_searcher(given, dictionary)

            lives = 0
            score = 0
            words_found = 0

            if difficulty == "EASY":
                lives = 10
            elif difficulty == "NORMAL":
                lives = 3
            elif difficulty == "DIFFICULT":
                lives = 5

            interface.print_anagram_searcher()

            while lives > 0 and len(anagram_list) > 0:
                interface.print_game_status_anagram(lives, words_found, score, given)
                word = str(input()).lower()
                if engine.word_checker(given, word, anagram_list):
                    score += engine.compute_score(word)
                    words_found +=1
                    anagram_list.remove(word)
                    interface.print_game_status_anagram(lives, words_found, score, given)
                else:
                    lives -= 1
                    interface.print_game_status_anagram(lives, words_found, score, given)

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

            difficulty = interface.choose_difficulty()

            lives = 0
            score = 0
            words_found = 0

            if difficulty == "EASY":
                lives = 5
                word_total = 2
            elif difficulty == "NORMAL":
                lives = 3
                word_total = 5
            elif difficulty == "DIFFICULT":
                lives = 5
                word_total = 10

            search_list = []
            while len(search_list) < word_total:
                x = random.choice(dictionary)
                if x not in search_list:
                    search_list.append(x)

            given = engine.char_generator(search_list)

            interface.print_word_finder()

            while lives > 0 and len(search_list) > 0:
                interface.print_game_status_wordfinder(lives, words_found, score, given)
                word = str(input()).lower()
                if engine.word_checker(given, word, dictionary):
                    score += engine.compute_score(word)
                    words_found +=1
                    search_list.remove(word)
                    interface.print_game_status_wordfinder(lives, words_found, score, given)
                else:
                    lives -= 1
                    interface.print_game_status_wordfinder(lives, words_found, score, given)

            if lives == 0:
                interface.clear_screen()
                print("YOU LOSE")
                input()
            else:
                interface.clear_screen()
                print("YOU WIN")
                input()
            menu = interface.main_menu()


exit()
