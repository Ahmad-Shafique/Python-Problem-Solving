import helper

def QuestionSeventeen():
	List = []
	amount = 0 
	helper.WhileInputActive(helper.PlaceInList,List)
	for item in List:
		string = ''
		Type = ''
		for num in item:
			if(num.isdigit()):
				string+=str(num)
			elif(num=='D') or (num=='W'):
				Type = num
		if(Type == 'D'):
			amount += int(string)
		else:
			amount -= int(string)
	print(int(amount))

	
QuestionSeventeen()