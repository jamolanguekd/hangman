def computing_scores(scrambled_letters):
    scrambled_letters_list = sorted(list(scrambled_letters))
    letter_scores = {'e':1,'a':1,'i':1,'o':1,'n':1,'r':1,'t':1,'l':1,'s':1,'u':1,'d':2,'g':2,'b':3,'c':3,'m':3,'p':3,'f':4,'h':4,'v':4,'y':4,'k':5,'j':8,'x':8,'q':10,'z':10}
    highest_possible_score = 0
    for word in all_words:
    	scrambled_letters_list_temp = [n for n in scrambled_letters_list]
    	word_score = 0
    	same_letter_counter = 0
    	for letter in word:
    		if letter in scrambled_letters_list_temp:
    			word_score += letter_scores[letter]
    			same_letter_counter += 1
    	if same_letter_counter == len(word):
    		highest_possible_score += word_score
    print(highest_possible_score)

filename = input()
fin = open(filename)
all_words = []
for line in fin:
	word = line.strip()
	all_words.append(word)

test_cases = int(input())

for i in range(test_cases):
    letter_str = input()
    computing_scores(letter_str)