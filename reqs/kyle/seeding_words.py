def  load_dictionary(filename):
    dictionary_file = open(filename)
    dictionary_list = []
    for line in dictionary_file.read().splitlines():
        dictionary_list.append(line)
    return dictionary_list


filename = str(input())
dictionary = load_dictionary(filename)

for word in dictionary:
    print(word)