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

            #new anagram mode code

            if difficulty == "EASY":  # for easy difficulty, only words with 4 letters or fewer will be used

                lives = 10
                easy_dictionary = []
                for word in dictionary:
                    if len(word) <= 4:
                        easy_dictionary.append(word)
                anagram_dictionary = [n for n in easy_dictionary]

            elif difficulty == "NORMAL":  # for normal difficulty, only words with 4 to 6 letters will be used

                lives = 5
                normal_dictionary = []
                for word in dictionary:
                    if 4 <= len(word) <= 6:
                        normal_dictionary.append(word)
                anagram_dictionary = [n for n in normal_dictionary]

            elif difficulty == "DIFFICULT":  # for difficult difficulty, only words with 6 letters or more will be used

                lives = 3
                difficult_dictionary = []
                for word in dictionary:
                    if len(word) >= 6:
                        difficult_dictionary.append(word)
                anagram_dictionary = [n for n in difficult_dictionary]

            while True:
                word_whose_anagrams_to_find = random.choice(anagram_dictionary)
                list_of_anagrams = engine.searching_for_anagrams(word_whose_anagrams_to_find, anagram_dictionary)
                if len(list_of_anagrams) > 0:
                    break

            #END new anagram mode code

            interface.print_anagram_searcher()

            score = 0
            words_found = 0

            #old anagram mode code
            '''
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
            
            '''

            # START new anagram mode code
            while lives > 0 and len(list_of_anagrams) > 0:
                interface.print_game_status_anagram(lives, words_found, len(list_of_anagrams), score,
                                                          word_whose_anagrams_to_find)
                word = str(input()).lower()
                if engine.word_checker(word_whose_anagrams_to_find, word, list_of_anagrams):
                    score += engine.compute_score(word)
                    words_found += 1
                    if word in list_of_anagrams:
                        list_of_anagrams.remove(word)
                    interface.print_game_status_anagram(lives, words_found, len(list_of_anagrams), score,
                                                              word_whose_anagrams_to_find)
                else:
                    lives -= 1
                    interface.print_game_status_anagram(lives, words_found, len(list_of_anagrams), score,
                                                              word_whose_anagrams_to_find)

            if lives == 0:
                interface.clear_screen()
                interface.print_you_lose()
                print("-------------------------------------------------------------------")
                print()
                print("The words you missed were: " + ", ".join(list_of_anagrams))
                print("Score: " + str(score))
                input()
            else:
                interface.clear_screen()
                interface.print_you_win()
                print("-------------------------------------------------------------------")
                print()
                print("Score: " + str(score))
                input()
            menu = interface.main_menu()

            # END new anagram mode code

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
