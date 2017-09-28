def WhileInputActive(function,List=None):
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


