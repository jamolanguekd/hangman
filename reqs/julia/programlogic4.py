def combining_words(word_str):
    letters_list = list(word_str)
    word_list = word_str.split()
    unique_letters_list = []
    for i in letters_list:
        if i != " " and i not in unique_letters_list:
            unique_letters_list.append(i)
    unique_letters_list.sort()
    final_output = []
    for i in unique_letters_list:
        largest_unique_letter_count = 0
        for j in word_list:
            letter_count = j.count(i)
            if letter_count > largest_unique_letter_count:
                largest_unique_letter_count = letter_count
        final_output.extend(largest_unique_letter_count*[i])
    print("".join(final_output))

filename = input()
test_cases = int(input())

for i in range(test_cases):
    word_str = input()
    combining_words(word_str)