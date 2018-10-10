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


filename = str(input())
dictionary = load_dictionary(filename)
test_cases = int(input())

for i in range(test_cases):
    word_pos = str(input())
    new_word_list = word_picker(dictionary, word_pos)
    for word in new_word_list:
        print(word, end=' ')
    print()
