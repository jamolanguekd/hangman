def load_dictionary(str_filename):
    dictionary_file = open(str_filename)
    dictionary_list = []
    for line in dictionary_file.read().splitlines():
        dictionary_list.append(line)
    return dictionary_list


def word_picker(list_dictionary, str_position):
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


def word_checker(str_char_seq, str_word, dictionary):
    char_seq_list = list(str_char_seq)
    if str_word not in dictionary:
        return False
    else:
        for letter in str_word:
            if letter in char_seq_list:
                char_seq_list.remove(letter)
            else:
                return False
        return True


filename = str(input())
dictionary = load_dictionary(filename)
test_cases = int(input())

for i in range(test_cases):
    word_input = str(input()).split()
    validity = word_checker(word_input[0], word_input[1], dictionary)
    if validity:
        print("True")
    else:
        print("False")
