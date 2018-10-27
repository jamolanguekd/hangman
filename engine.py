def load_dictionary(filename):
    dictionary_file = open(filename)
    dictionary_list = []
    for line in dictionary_file.read().splitlines():
        dictionary_list.append(line)
    return dictionary_list


def pick_words(list_dictionary, str_position):
    position_list = str_position.split()
    word_list = []
    for position in position_list:
        word_list.append(list_dictionary[int(position)])
    return word_list


def anagram_searcher(str_word_input, list_dictionary):
    sorted_word = ''.join(sorted(str_word_input))
    anagram_list = []
    for word in list_dictionary:
        if ''.join(sorted(word)) == sorted_word:
            anagram_list.append(word)
    if str_word_input not in anagram_list:
        anagram_list.append(str_word_input)
    anagram_list.sort()
    return anagram_list


def char_generator(str_word_input):
    word_list = str_word_input.split()
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
            count += 1
        elif letter in two:
            count += 2
        elif letter in three:
            count += 3
        elif letter in four:
            count += 4
        elif letter in five:
            count += 5
        elif letter in eight:
            count += 8
        elif letter in ten:
            count += 10

    return count
