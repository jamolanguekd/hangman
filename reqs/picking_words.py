def  load_dictionary(filename):
    dictionary_file = open(filename)
    dictionary_list = []
    for line in dictionary_file.read().splitlines():
        dictionary_list.append(line)
    return dictionary_list

def word_picker(dictionary,position):
    position = position.split()
    word_list = []
    for item in position:
        word_list.append(dictionary[int(item)])
    return word_list




filename = str(input())
dictionary = load_dictionary(filename)
test_cases = int(input())

for i in range(test_cases):
    word_pos = str(input())
    word_list = word_picker(dictionary,word_pos)
    for item in word_list:
        print(item,end=' ')
    print()