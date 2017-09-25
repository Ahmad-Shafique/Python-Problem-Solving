	

def WhileInput(func):
	while True:
		i=input()
		if(i!=os.linesep):
			func(int(i))
		else:
			break

	
dictionary=dict()	

def AddDictionaryItem(item):
	dictionary[item] = item*item

	
WhileInput(AddDictionaryItem)

print(dictionary)

