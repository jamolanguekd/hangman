def searching_for_anagrams(filename,word):
    final_output = []
    for i in all_words:
        i_letters = [n for n in i]
        i_letters.sort()
        word_letters = [n for n in word]
        word_letters.sort()
        if i_letters == word_letters:
            final_output.append(i)
    print(" ".join(final_output))

filename = input()
test_cases = int(input())

fin = open(filename)
all_words = []
for line in fin:
    words = line.strip()
    all_words.append(words)

for i in range(test_cases):
    word = input()
    searching_for_anagrams(filename,word)