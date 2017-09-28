def biggerSize(input,sizeX):
	if(input.isalnum()):
		return input * sizeX
	elif(input.isdigit()):
		input = str(input)
		input = input*sizeX
		return int(input)
def QuestionFifteen():
	Input = input();
	result = int(Input) + int(biggerSize(Input,2))+ int(biggerSize(Input,3))+ int(biggerSize(Input,4))
	print(result)

	
QuestionFifteen()