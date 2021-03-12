#you may NOT change the signature of the existing functions.

SUBMISSION_IDS = ["316296771"]

#Question 4a
def num_different_letters(text):
	text = str(text)
	chars = "abcdefghijklmnopqrstuvwxyz"
	unique_letters = 0
	for letter in chars : #going through each letter in the a-z
		cnt = 0
		for compare_letter in text :
			if letter == compare_letter :
				cnt += 1
			if cnt > 1:
				break
		if cnt > 0 :
			unique_letters += 1
	return unique_letters

#Question 4b
def max_letter_count(text):
	text = str(text)
	chars = "abcdefghijklmnopqrstuvwxyz"
	max_cnt = 0
	for letter in chars : #going through each letter in the a-z
		cnt = 0
		for compare_letter in text:
			if letter == compare_letter:
				cnt += 1
		if cnt > max_cnt :
			max_cnt = cnt
	return max_cnt

#Question 4c
def is_legal(text):
	chars = "abcdefghijklmnopqrstuvwxyz"
	nums = "0123456789"
	text = str(text)
	lst = text.split()
	legal = True
	for word in lst: #checking each word in the list
		cnt_nums = 0
		cnt_letters = 0

		for note in word: #going through each letter
			for compare_nums in nums: #checking if the letter is num
				if note==compare_nums:
					cnt_nums += 1
					break
			
			for compare_letters in chars: #checking if the letter is text
				if note==compare_letters:
					cnt_letters += 1
					break
			if cnt_nums>0 and cnt_letters>0: #just for efficiency
				break
		if cnt_nums>0 and cnt_letters>0: #checking if there are nums&letters in the word
			legal = False
			break
	return legal

#Question 4d
def is_palindrome(text):
	text = str(text)
	palindrome = True
	left_letter = 0
	right_letter = int(len(text)) - 1
	while left_letter < right_letter:
		if text[left_letter] != text[right_letter]:
			palindrome=False
			break
		left_letter += 1
		right_letter -= 1
	return palindrome

#Question 5
def calc(expression):
	exp = expression.split("'")
	result = exp[1] # first index is '' - a0 is in [1]
	for i in range(2, len(exp), 2): #every second index is a calc expression - */+
		if exp[i]=="*":
			result = result*int(exp[i+1])
		if exp[i]=="+":
			result = result+exp[i+1]
			i=i+2
	return result

#Question 6
def max_div_seq(n, k):
	n=str(n)
	max_cnt = 0
	for i in range(len(n)):
		cnt = 0
		number = n[i]
		j = 1
		while (int(number)%k) == 0:
			cnt+=1
			if (i+j)==len(n):
				break
			number = str(number)+n[i+j]
			j += 1
		if max_cnt < cnt:
			max_cnt = cnt
	return max_cnt

########
# Tester
########

def test():
    #testing Q4
    if num_different_letters("aa bb cccc dd ee fghijklmnopqrstuvwxyz") != 26:
        print("error in num_different_letters - 1")

    if max_letter_count("aa bb cccc dd ee fghijklmnopqrstuvwxyz") != 4:
        print("error in max_letter_count - 1")

    if not is_legal("number 34 says hi to number 43"):
        print("error in is_legal - 1")

    if not is_palindrome("1step on no pets1"):
        print("error in is palindrome - 1")

    #testing Q5
    if calc("'123321'*'2'") != "123321123321":
        print("error in calc - 1")
    if calc("'Hi there '*'3'+'you2'") != "Hi there Hi there Hi there you2":
        print("error in calc - 2")
        
    #testing Q6
    l = max_div_seq(23300247524689, 2)
    if l != 4:
        print("Error in max_div_seq")

    if not SUBMISSION_IDS:
        print("The list of IDs is empty")
        
    if not type(SUBMISSION_IDS) == list:
        print("The list of IDs is not a list type")

    if SUBMISSION_IDS and not all(type(x)==str for x in SUBMISSION_IDS):
        print("The list of IDs contains elments that are not strings")
