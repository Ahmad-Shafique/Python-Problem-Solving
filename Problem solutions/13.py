
def checkNumberOfDigits(string):
	number = 0
	for item in string:
		if item.isdigit():
			number +=1
	return number

def checkNumberOfLetters(string):
	number = 0
	for item in string:
		if item.isalpha():
			number +=1
	return number


def QuestionThiteen():
	Input = input();
	letters = checkNumberOfLetters(Input);
	digits = checkNumberOfDigits(Input);
	print('LETTERS '+ str(letters));
	print('DIGITS' + str(digits));

	
QuestionThiteen()

