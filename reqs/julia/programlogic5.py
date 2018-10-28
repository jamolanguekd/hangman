def checking_words(letters,word):
    scrambled_letters_list = sorted(list(scrambled_letters))
    word_letters_list = sorted(list(word_entered))
    both_in_word_and_scrambled_letters = []
    for i in word_letters_list:
        if i in scrambled_letters_list:
            both_in_word_and_scrambled_letters.append(i)
    if both_in_word_and_scrambled_letters == word_letters_list and word_entered in all_words:
        print("True")
    else:
        print("False")

filename = input()
fin = open(filename)
all_words = []
for line in fin:
    word = line.strip()
    all_words.append(word)

test_cases = int(input())

for i in range(test_cases):
    input_list = input().split()
    scrambled_letters = input_list[0]
    word_entered = input_list[1]
    checking_words(scrambled_letters,word_entered)