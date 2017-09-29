def ListGenerator(Rule,initialLimit,finalLimit):
	for value in range(initialLimit,finalLimit+1):
		if(Rule(value)):
			yield value
def Rule(value):
	if(value%7 == 0):
		return True
	else:
		return False

def QuestionTwenty():
	userInput = input()
	for value in ListGenerator(Rule,0,int(userInput)):
		print(value)

		
QuestionTwenty()
