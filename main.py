import interface
import engine
import random

dictionary = engine.load_dictionary("dictionary.txt")
menu = ""
mode = ""
difficulty = ""

lives = 0

# GAME WILL RUN UNTIL THE USER QUITS FROM THE MAIN MENU
while menu != "QUIT":

    menu = interface.main_menu()

    # WHEN THE USER PRESSES START
    while menu == "START":

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
                            # VALID ATTEMPT
                            if engine.attempt_checker(input_word, list_correct_guesses):
                                list_anagrams_left.remove(input_word)
                                score += engine.compute_score(input_word)
                                words_found += 1

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
                    # USER WANTS TO CONTINUE
                    # do nothing

                    # USER WANTS TO END
                    if not continue_state:
                        mode = ""

        while mode == "WORD FINDER":

            interface.print_word_finder()

            score = 0
            words_found = 0

            # USER SELECTS DIFFICULTY
            difficulty = interface.choose_difficulty()
            lives = engine.generate_lives(mode, difficulty)
            word_total = engine.generate_word_total(difficulty)

            # GENERATE WORD LIST
            wordfinder_dictionary = engine.generate_wordfinder_dict(difficulty, dictionary)

            continue_state = True

            while continue_state:

                list_positions = engine.generate_positions(word_total, wordfinder_dictionary)
                list_words = engine.picking_words_wordfinder(wordfinder_dictionary, list_positions)
                list_words_left = list_words.copy()

                given_word = engine.char_generator(list_words_left)

                # WORDS TO FIND WITH BLANKS
                list_blank = engine.generate_blanks(list_words_left)

                interface.print_word_finder()

                list_correct_guesses = []
                list_bonus_guesses = []
                list_incorrect_guesses = []

                while lives > 0 and len(list_words_left) > 0:

                    interface.print_wordfinder_status(lives, words_found, len(list_words_left), score, given_word,
                                                      list_blank, list_bonus_guesses, list_incorrect_guesses)

                    input_word = str(input()).lower()

                    # USER DECIDES TO EXIT MIDGAME
                    if input_word == "1":
                        continue_state = False
                        mode = ""
                        break

                    # USER ATTEMPTS A GUESS
                    else:

                        # CORRECT ATTEMPT
                        if engine.word_checker_wordfinder(given_word, input_word, list_words):

                            # VALID ATTEMPT
                            if engine.attempt_checker(input_word, list_correct_guesses):
                                list_words_left.remove(input_word)
                                score += engine.compute_score(input_word)
                                words_found += 1

                        # BONUS ATTEMPT
                        elif engine.word_checker_wordfinder(given_word, input_word, dictionary):

                            # VALID ATTEMPT
                            if engine.attempt_checker(input_word, list_bonus_guesses):
                                score += engine.compute_score(input_word)

                        # INCORRECT ATTEMPT
                        else:
                            if engine.attempt_checker(input_word, list_incorrect_guesses):
                                lives -= 1

                        list_blank = engine.update_blanks(list_blank, list_correct_guesses, list_words)
                        interface.print_wordfinder_status(lives, words_found, len(list_words_left), score, given_word,
                                                          list_blank, list_bonus_guesses, list_incorrect_guesses)

                # USER LOSES
                if lives == 0 and input_word != "1":
                    continue_state = interface.continue_game(False, list_words_left, score)

                    # USER STILL WANTS TO PLAY WORD FINDER
                    if continue_state:
                        break

                    # USER DOESNT WANNA PLAY ANYMORE
                    else:
                        mode = ""
                        break

                # USER WINS
                elif lives > 0 and input_word != "1":
                    continue_state = interface.continue_game(True, list_words_left, score)

                    # USER STILL WANTS TO PLAY
                    # do nothing

                    # USER DOESN'T WANT TO PLAY
                    if not continue_state:
                        mode = ""

        while mode == "BACK":
            mode = ""

        menu = ""

    # WHEN THE USER PRESSES HELP
    while menu == "HELP":

        mode = interface.help()

        if mode == "BACK":
            menu = ""
            break

exit()
