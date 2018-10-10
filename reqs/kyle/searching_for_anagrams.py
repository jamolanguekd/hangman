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


filename = str(input())
dictionary = load_dictionary(filename)
test_cases = int(input())

for i in range(test_cases):
    word_input = str(input())
    matching_words = anagram_searcher(word_input, dictionary)

    for item in matching_words:
        print(item, end=' ')
    print()
