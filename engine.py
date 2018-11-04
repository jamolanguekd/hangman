import random


def load_dictionary(str_filename):
    dictionary_file = open(str_filename)
    dictionary_list = []
    for line in dictionary_file.read().splitlines():
        dictionary_list.append(line)
    return dictionary_list


def picking_words_wordfinder(list_dictionary, list_position):
    word_list = []
    for position in list_position:
        word_list.append(list_dictionary[int(position)])
    return word_list


def picking_words_anagram(list_dictionary):
    word = random.choice(list_dictionary)
    return word


def generate_blanks(list_words):
    list_blank = []
    for word in list_words:
        ch = list(word)
        for i in range(len(ch)):
            ch[i] = "_"

        if len(ch) <= 4:
            revealed_count = 2

        elif 4 < len(ch) <= 7:
            revealed_count = 3

        else:
            revealed_count = 4

        while ch.count("_") != len(ch) - revealed_count:
            while True:
                pos = random.randint(0, len(ch) - 1)
                if ch[pos] == "_":
                    break
            ch[pos] = word[pos]
        list_blank.append(" ".join(ch))

    return list_blank


def update_blanks(list_blank, list_correct_guesses, list_words):
    for guess in list_correct_guesses:
        list_blank[list_words.index(guess)] = guess

    return list_blank


def generate_positions(int_words_total, list_dict):
    position_list = []
    while len(position_list) < int_words_total:
        pos = random.randint(0, len(list_dict)-1)
        if pos not in position_list:
            position_list.append(pos)
    return position_list


def generate_lives(str_mode, str_difficulty):
    if str_mode == "ANAGRAM SEARCHER":
        if str_difficulty == "EASY":
            lives = 10
        elif str_difficulty == "NORMAL":
            lives = 5
        elif str_difficulty == "DIFFICULT":
            lives = 3

    elif str_mode == "WORD FINDER":
        if str_difficulty == "EASY":
            lives = 10
        elif str_difficulty == "NORMAL":
            lives = 5
        elif str_difficulty == "DIFFICULT":
            lives = 3

    return lives


def generate_word_total(str_difficulty):
    word_total = 0
    if str_difficulty == "EASY":
        word_total = 5
    elif str_difficulty == "NORMAL":
        word_total = 5
    elif str_difficulty == "DIFFICULT":
        word_total = 5
    return word_total


def generate_wordfinder_dict(str_difficulty, list_dict):
    wordfinder_dictionary = []
    if str_difficulty == "EASY":
        for word in list_dict:
            if len(word) <= 4:
                wordfinder_dictionary.append(word)

    elif str_difficulty == "NORMAL":
        for word in list_dict:
            if len(word) <= 6:
                wordfinder_dictionary.append(word)
                wordfinder_dictionary.append(word)

    elif str_difficulty == "DIFFICULT":  # difficult mode includes all words
        wordfinder_dictionary = list_dict.copy()

    return wordfinder_dictionary


def generate_anagram_dict(str_difficulty, list_dict):
    anagram_dictionary = []
    if str_difficulty == "EASY":
        for word in list_dict:
            if 3 <= len(word) <= 4:
                anagram_dictionary.append(word)

    elif str_difficulty == "NORMAL":
        for word in list_dict:
            if 3<= len(word) <=5:
                anagram_dictionary.append(word)

    elif str_difficulty == "DIFFICULT":
        for word in list_dict:
            if 3<= len(word) <=6:
                anagram_dictionary.append(word)
    return anagram_dictionary


def searching_for_anagrams(list_dictionary, str_word):
    anagram_list = []
    word_letters = sorted([n for n in str_word])
    for i in list_dictionary:
        i_letters = sorted([n for n in i])
        if i_letters == word_letters and i != str_word:
            anagram_list.append(i)
    return anagram_list


def char_generator(list_words):
    word_list = [n for n in list_words]
    char_seq = []
    for word in word_list:
        for letter in word:
                if word.count(letter) > char_seq.count(letter):
                    char_seq.append(letter)
    char_seq = ''.join(sorted(char_seq))
    return char_seq


def word_checker_wordfinder(str_char_seq, str_word, list_dictionary):
    char_seq_list = list(str_char_seq)
    if str_word not in list_dictionary:
        return False
    else:
        for letter in str_word:
            if letter in char_seq_list:
                char_seq_list.remove(letter)
            else:
                return False
        return True


# SHUFFLES THE GIVEN STRING IN WORD FINDER MODE

def wordfinder_shuffle(str_char_seq):
    char_list = list(str_char_seq)
    random.shuffle(char_list)
    new_str_char_seq = "".join(char_list)
    return new_str_char_seq


def word_checker_anagram(str_input_word, list_anagrams):
    if str_input_word in list_anagrams:
        return True
    return False


# CHECKS IF ATTEMPT IS VALID

def attempt_checker(str_input_word, list_guesses):
    if str_input_word in list_guesses:
        return False
    else:
        list_guesses.append(str_input_word)
    return True



def compute_score(str_word):
    one = ['e', 'a', 'i', 'o', 'n', 'r', 't', 'l', 's', 'u']
    two = ['d', 'g']
    three = ['b', 'c', 'm', 'p']
    four = ['f', 'h', 'v', 'w', 'y']
    five = ['k']
    eight = ['j', 'x']
    ten = ['q', 'z']

    count = 0
    for letter in str_word:
        if letter in one:
            count += 100
        elif letter in two:
            count += 200
        elif letter in three:
            count += 300
        elif letter in four:
            count += 400
        elif letter in five:
            count += 500
        elif letter in eight:
            count += 800
        elif letter in ten:
            count += 1000

    return count


#commented out the function that writes a file
'''
if __name__ == '__main__':

    import interface

    dictionary = load_dictionary("dictionary.txt")
    new_file = open("anagram_count.txt", 'w')
    for word in dictionary:
        new_file.write(str(len(anagram_searcher(word, dictionary))))
        interface.progress(dictionary.index(word)+1, len(dictionary), str(dictionary.index(word)+1)+"/"+str(len(dictionary)))
'''
