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
        while mode == "ANAGRAM SEARCHER":

            interface.print_anagram_searcher()

            score = 0
            words_found = 0

            # USER SELECTS DIFFICULTY
            difficulty = interface.choose_difficulty()
            lives = engine.generate_lives(mode, difficulty)
            anagram_dictionary = engine.generate_anagram_dict(difficulty, dictionary)

            continue_state = True

            # WHILE THE USER HAS AND WANTS TO CONTINUE PLAYING
            while continue_state:
                list_anagrams = []
                while len(list_anagrams) == 0:
                    given_word = engine.picking_words_anagram(anagram_dictionary)
                    list_anagrams = engine.searching_for_anagrams(anagram_dictionary, given_word)
                list_anagrams_left = list_anagrams.copy()
                list_correct_guesses = []
                list_incorrect_guesses = []

                while lives > 0 and len(list_anagrams_left) > 0:
                    interface.print_anagram_status(lives, words_found, len(list_anagrams_left), score,
                                                   given_word, list_correct_guesses,
                                                   list_incorrect_guesses)
                    input_word = str(input()).lower()

                    # USER CHOOSES TO EXIT MID-GAME
                    if input_word == "1":
                        continue_state = False
                        mode = ''
                        break

                    # USERS ATTEMPTS TO ANSWER
                    else:

                        # CORRECT ATTEMPT
                        if engine.word_checker_anagram(input_word, list_anagrams):
                            list_anagrams_left.remove(input_word)
                            # VALID ATTEMPT
                            if engine.attempt_checker(input_word, list_correct_guesses):
                                score += engine.compute_score(input_word)
                                words_found += 1
                            interface.print_anagram_status(lives, words_found, len(list_anagrams_left), score,
                                                           given_word, list_correct_guesses,
                                                           list_incorrect_guesses)

                        # INCORRECT ATTEMPT
                        else:
                            if engine.attempt_checker(input_word, list_incorrect_guesses):
                                lives -= 1
                            interface.print_anagram_status(lives, words_found, len(list_anagrams_left), score,
                                                           given_word, list_correct_guesses,
                                                           list_incorrect_guesses)

                # USER LOSES
                if lives == 0 and input_word != "1":
                        continue_state = interface.continue_game(False, list_anagrams_left, score)

                        # USER WANTS TO PLAY ANAGRAM AGAIN
                        if continue_state:
                            break

                        # USER DOESN'T WANT TO PLAY ANAGRAMS ANYMORE
                        else:
                            mode = ""
                            break

                # USER WINS
                elif lives > 0 and input_word != "1":
                    continue_state = interface.continue_game(True, list_anagrams_left, score)
                    mode = ""

        menu = interface.main_menu()

        while mode == "WORD FINDER":

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
                for input_word in dictionary:
                    if len(input_word) <= 4:
                        easy_dictionary.append(input_word)
                scramble_dictionary = [n for n in easy_dictionary]
            elif difficulty == "NORMAL":  # normal mode includes words with 6 letters and fewer
                lives = 5
                word_total = 5
                normal_dictionary = []
                for input_word in dictionary:
                    if len(input_word) <= 6:
                        normal_dictionary.append(input_word)
                scramble_dictionary = [n for n in normal_dictionary]
            elif difficulty == "DIFFICULT":  # difficult mode includes all words
                lives = 3
                word_total = 5
                scramble_dictionary = [n for n in dictionary]

            search_list = engine.picking_words_wordfinder(scramble_dictionary, random.sample(range(0, len(scramble_dictionary) - 1), word_total))
            search_list_copy = search_list.copy()

            given = engine.char_generator(search_list)

            # WORDS TO FIND WITH BLANKS
            found_list = []
            for input_word in search_list:
                x = list(input_word)
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
                    x[pos] = input_word[pos]
                found_list.append("".join(x))

            interface.print_word_finder()

            list_correct_guesses = []
            bonus_words_inputted= []
            list_incorrect_guesses = []
            while lives > 0 and len(search_list) > 0:
                interface.print_wordfinder_status(lives, words_found, len(search_list), score, given, list_correct_guesses, bonus_words_inputted, list_incorrect_guesses)
                for item in found_list:
                    print(item)
                input_word = str(input()).lower()

                if input_word== "1":
                    #menu = interface.main_menu()
                    break
                else:
                    if engine.word_checker(given, input_word, dictionary):

                        score += engine.compute_score(input_word)
                        words_found += 1
                        if input_word in search_list:

                            if input_word not in list_correct_guesses:
                                list_correct_guesses.append(input_word)

                            found_list[search_list_copy.index(input_word)] = input_word
                            search_list.remove(input_word)
                            given = engine.char_generator(search_list)
                        else:
                            if input_word not in bonus_words_inputted:
                                bonus_words_inputted.append(input_word)

                    else:
                        lives -= 1
                        if input_word not in list_incorrect_guesses:
                            list_incorrect_guesses.append(input_word)

                    interface.print_wordfinder_status(lives, words_found, len(search_list), score, given,
                                                      list_correct_guesses, bonus_words_inputted, list_incorrect_guesses)

            if lives == 0 and input_word!= "1":
                interface.clear_screen()
                interface.print_you_lose(search_list, score)
                input()
            elif lives>0 and input_word!= "1":
                interface.clear_screen()
                interface.print_you_win(score)
                input()

            menu = interface.main_menu()

        while mode == "BACK":
            menu = interface.main_menu()
            break

    elif menu == "HELP":
        mode = interface.help()

        if mode == "BACK":
            menu = interface.main_menu()

exit()
