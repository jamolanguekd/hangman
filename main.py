import interface
import engine
import random
import itertools

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

            #original anagram mode code
            '''
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
            '''

            interface.print_anagram_searcher()

            while lives > 0 and len(anagram_list) > 0:
                interface.print_game_status_anagram(lives, words_found, len(anagram_list), score, given)
                word = str(input()).lower()
                if engine.word_checker(given, word, anagram_list):
                    score += engine.compute_score(word)
                    words_found += 1
                    if word in anagram_list:
                        anagram_list.remove(word)
                    interface.print_game_status_anagram(lives, words_found, len(anagram_list), score, given)
                else:
                    lives -= 1
                    interface.print_game_status_anagram(lives, words_found, len(anagram_list), score, given)

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
            word_total = 0
            if difficulty == "EASY":
                lives = 10
                word_total = 2
            elif difficulty == "NORMAL":
                lives = 3
                word_total = 3
            elif difficulty == "DIFFICULT":
                lives = 5
                word_total = 5

            search_list = engine.pick_words(dictionary, random.sample(range(0, len(dictionary)-1), word_total))
            search_list_copy = search_list.copy()

            given = engine.char_generator(search_list)

            # WORDS TO FIND WITH BLANKS
            found_list = []
            for word in search_list:
                x = list(word)
                for i in range(len(x)):
                    x[i] = "_"

                revealed_count = 0
                if len(x) <= 4:
                    revealed_count = 2

                elif 4 < len(x) <= 8:
                    revealed_count = 4

                while x.count("_") != len(x) - revealed_count:
                    pos = 0
                    while x[pos] != "_":
                        pos = random.randint(0, len(x)- 1)
                    x[pos] = word[pos]
                found_list.append("".join(x))

            interface.print_word_finder()

            while lives > 0 and len(search_list) > 0:
                interface.print_game_status_wordfinder(lives, words_found, len(search_list), score, given)
                for item in found_list:
                    print(item)
                word = str(input()).lower()
                if engine.word_checker(given, word, dictionary):
                    score += engine.compute_score(word)
                    words_found += 1
                    if word in search_list:
                        found_list[search_list_copy.index(word)] = word
                        search_list.remove(word)
                        given = engine.char_generator(search_list)

                    interface.print_game_status_wordfinder(lives, words_found, len(search_list), score, given)
                else:
                    lives -= 1
                    interface.print_game_status_wordfinder(lives, words_found, len(search_list), score, given)

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
