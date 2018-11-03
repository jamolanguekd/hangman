import interface
import engine
import random

dictionary = engine.load_dictionary("dictionary.txt")
menu = interface.main_menu()
mode = ""
difficulty = ""

lives = 0

# GAME WILL RUN UNTIL THE USER QUITS FROM THE MAIN MENU
while menu != "QUIT":

    # WHEN THE USER PRESSES START
    if menu == "START":

        mode = interface.choose_mode()

        # SELECT ANAGRAM SEARCHER
        if mode == "ANAGRAM SEARCHER":

            interface.print_anagram_searcher()

            score = 0
            words_found = 0

            difficulty = interface.choose_difficulty()

            lives = engine.generate_lives(mode, difficulty)
            anagram_dictionary = engine.generate_anagram_dict(difficulty, dictionary)

            while True:
                word_whose_anagrams_to_find, list_of_anagrams = engine.searching_for_anagrams(anagram_dictionary)

                right_words_inputted = []
                wrong_words_inputted = []
                state = True

                while lives > 0 and len(list_of_anagrams) > 0:
                    interface.print_game_status_anagram(lives, words_found, len(list_of_anagrams), score,
                                                              word_whose_anagrams_to_find, right_words_inputted, wrong_words_inputted)
                    word = str(input()).lower()

                    if word == "1":
                        state = False
                        break

                    else:
                        if engine.word_checker(word_whose_anagrams_to_find, word, list_of_anagrams):
                            score += engine.compute_score(word)
                            words_found += 1
                            if word in list_of_anagrams:
                                list_of_anagrams.remove(word)
                                if word not in right_words_inputted:
                                    right_words_inputted.append(word)
                            interface.print_game_status_anagram(lives, words_found, len(list_of_anagrams), score,
                                                                      word_whose_anagrams_to_find, right_words_inputted, wrong_words_inputted)
                        else:
                            lives -= 1
                            if word not in wrong_words_inputted:
                                wrong_words_inputted.append(word)
                            interface.print_game_status_anagram(lives, words_found, len(list_of_anagrams), score,
                                                                      word_whose_anagrams_to_find, right_words_inputted, wrong_words_inputted)

                    if lives == 0 and word!="1":
                        interface.print_you_lose(list_of_anagrams, score)
                        break
                    elif lives > 0 and word != "1":
                        interface.print_you_win(score)
                        continue_value = interface.continue_game()
                        if continue_value == 2:
                            break
                    menu = "START"

                if state==False:
                    menu = interface.main_menu()
                    break

        elif mode == "WORD FINDER":

            difficulty = interface.choose_difficulty()

            lives = 0
            score = 0
            words_found = 0
            word_total = 0
            scramble_dictionary = []

            if difficulty == "EASY":  # easy mode includes only words with 4 letters and fewer
                lives = 10
                word_total = 5
                easy_dictionary = []
                for word in dictionary:
                    if len(word) <= 4:
                        easy_dictionary.append(word)
                scramble_dictionary = [n for n in easy_dictionary]
            elif difficulty == "NORMAL":  # normal mode includes words with 6 letters and fewer
                lives = 5
                word_total = 5
                normal_dictionary = []
                for word in dictionary:
                    if len(word) <= 6:
                        normal_dictionary.append(word)
                scramble_dictionary = [n for n in normal_dictionary]
            elif difficulty == "DIFFICULT":  # difficult mode includes all words
                lives = 3
                word_total = 5
                scramble_dictionary = [n for n in dictionary]

            search_list = engine.pick_words(scramble_dictionary, random.sample(range(0, len(scramble_dictionary)-1), word_total))
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

            right_words_inputted = []
            bonus_words_inputted= []
            wrong_words_inputted = []
            while lives > 0 and len(search_list) > 0:
                interface.print_game_status_wordfinder(lives, words_found, len(search_list), score, given,right_words_inputted,bonus_words_inputted,wrong_words_inputted)
                for item in found_list:
                    print(item)
                word = str(input()).lower()

                if word=="1":
                    #menu = interface.main_menu()
                    break
                else:
                    if engine.word_checker(given, word, dictionary):

                        score += engine.compute_score(word)
                        words_found += 1
                        if word in search_list:

                            if word not in right_words_inputted:
                                right_words_inputted.append(word)

                            found_list[search_list_copy.index(word)] = word
                            search_list.remove(word)
                            given = engine.char_generator(search_list)
                        else:
                            if word not in bonus_words_inputted:
                                bonus_words_inputted.append(word)

                    else:
                        lives -= 1
                        if word not in wrong_words_inputted:
                            wrong_words_inputted.append(word)

                    interface.print_game_status_wordfinder(lives, words_found, len(search_list), score, given,
                                                               right_words_inputted, bonus_words_inputted, wrong_words_inputted)

            if lives == 0 and word!="1":
                interface.clear_screen()
                interface.print_you_lose(search_list, score)
                input()
            elif lives>0 and word!="1":
                interface.clear_screen()
                interface.print_you_win(score)
                input()

            menu = interface.main_menu()

        elif mode == "BACK":
            menu= interface.main_menu()

    elif menu == "HELP":
        state = interface.help()
        if state == "BACK":
            menu = "START"



exit()