import random


def load_dictionary(filename):
    dictionary_file = open(filename)
    dictionary_list = []
    for line in dictionary_file.read().splitlines():
        dictionary_list.append(line)
    return dictionary_list


# PICKING WORDS FOR WORDFINDER
def picking_words(list_dictionary, list_position):
    word_list = []
    for position in list_position:
        word_list.append(list_dictionary[int(position)])
    return word_list


# PICKING WORDS FOR ANAGRAM
def picking_words(list_dictionary):
    word = random.choice(list_dictionary)
    return word


def generate_lives(mode, difficulty):
    if mode == "ANAGRAM SEARCHER":
        if difficulty == "EASY":
            lives = 10
        elif difficulty == "NORMAL":
            lives = 5
        elif difficulty == "DIFFICULT":
            lives = 3

    return lives


def generate_anagram_dict(difficulty, dictionary):
    if difficulty == "EASY":
        anagram_dictionary = []
        for word in dictionary:
            if len(word) <= 4:
                anagram_dictionary.append(word)
    elif difficulty == "NORMAL":
        anagram_dictionary = []
        for word in dictionary:
            if 4 < len(word) <= 7:
                anagram_dictionary.append(word)
    elif difficulty == "DIFFICULT":
        anagram_dictionary = []
        for word in dictionary:
            if len(word) > 7:
                anagram_dictionary.append(word)
    return anagram_dictionary


def searching_for_anagrams(list_dictionary, str_word):
    while True:
        anagram_list = []
        word_letters = sorted([n for n in str_word])
        for i in list_dictionary:
            i_letters = sorted([n for n in i])
            if i_letters == word_letters and i != str_word:
                anagram_list.append(i)
        if len(anagram_list) > 0:
            break

    return anagram_list


def char_generator(list_words):
    word_list = list_words
    char_seq = []
    for word in word_list:
        for letter in word:
                if word.count(letter) != char_seq.count(letter):
                    char_seq.append(letter)
    char_seq = ''.join(sorted(char_seq))
    return char_seq


def word_checker(str_char_seq, str_word, list_dictionary):
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
