def seeding_words(filename):
    fin = open(filename)
    for line in fin:
        word = line.strip()
        print(word)

filename = input()
seeding_words(filename)