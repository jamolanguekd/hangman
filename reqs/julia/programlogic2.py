def picking_words(filename):
    final_output = []
    for i in word_positions:
        final_output.append(all_words[i])
    print(" ".join(final_output))

filename = input()
test_cases = int(input())
fin = open(filename)
all_words = []
for line in fin:
    word = line.strip()
    all_words.append(word)

for i in range(test_cases):
    word_positions = [int(n) for n in input().split()]
    picking_words(filename)