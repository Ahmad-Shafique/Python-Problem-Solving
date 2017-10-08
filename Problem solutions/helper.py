def WhileInputActive(function,List=None):
	'''Function To take inputs continuously
	'''
	while True:
                inputVariable = input();
                if (inputVariable is None) or (not inputVariable):
                        break;
                if (List is None):
                        function(inputVariable);
                else:
                        function(List,inputVariable);



def PlaceInList(List,Input):
	List.append(Input);



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

def ListGenerator(Rule,initialLimit,finalLimit):
	for value in range(int(initialLimit),int(finalLimit)+1):
		if(Rule(value)):
			yield value

def ConvertToUsableFilePath(filePath):
	newFilePath=""
	for char in filePath:
		if(char != '\\'):
			newFilePath += char
		else:
			newFilePath+='\\\\'
	return newFilePath



#str[::-1] reverses the string
#str[::2] collects all characters at even indices
#str[::1] collects all characters at odd indices
#where str is the string