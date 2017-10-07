# Sample run of level one csv to json
# CSV to JSON at level one

def CSVToJSONLOne(string, attr = [1,2,3]):
	newStr = "{"
	list = string.split(",")
	length = len(attr)
	for item in attr:
		newStr+='"'
		newStr += str(item)
		newStr+='"'
		newStr+=":"
		newStr+='"'
		newStr += str(list[attr.index(item)])
		newStr+='"'
		if((int(attr.index(item))) != (int(length-1))):
			newStr+=","
	newStr+="}"
	return newStr
#
#
#
#




#
# Incomplete functionality
#
# Separate out dictionaries

def AppendDictionaries(mainDictionary, newDictionary):
	if mainDictionary == None:
		mainDictionary = newDictionary
	else:
		mainDictionary = {**mainDictionary,**newDictionary}
	return mainDictionary

def SeparateDictionaries(string):
	dictionary = {}
	list = string.split(",")
	for item in list:
		#print("outer loop")
		newDItem = dict()
		nName = ""
		nNameAttribute = ""
		subString = str(item)
		flag = 1
		for sItem in subString:
			#print("inner loop:: sItem = " + str(sItem))
			if(sItem == '|'):
				nName += str(sItem)
			else:
				if(sItem == '_'):
					continue
				nNameAttribute +=str(sItem)
				flag = 2
		if(flag == 1):
			newDItem[str(nName)] = None
			#print('nName = ' + nName)
			dictionary = {**dictionary,**newDItem}
		elif(flag == 2 ):
			newDItem[str(nNameAttribute)] = None
			dictionary[str(nName)] = AppendDictionaries(dictionary[str(nName)], newDItem)
			#print('nName = ' + nName)
			#print('nNameAttribute = ' + nNameAttribute)
	return dictionary


def ReturnStringBefore(string,parameter):
	nString = ""
	for i in string:
		if(i!=parameter):
			nString +=  i
		else:
			break
	return nString

def ReturnStringAfter(string,parameter):
	nString = ""
	for i in reversed(string):
		if(i!=parameter):
			nString =  i+nString
		else:
			break
	return nString

def CheckRegexEquality(regex,string):
	import re
	if(re.match(regex,string)):
		return True
	else:
		return False

def AppendItemsIntoList(*args):
	List = []
	for item in args:
		List.append(item)
	return List

def SameTypeDictionaries(dictionaryOne,dictionaryTwo):
	if(dictionaryOne.keys()  == dictionaryTwo.keys()):
		return True
	else:
		return False

def AppendKeyToDictionary(dictionary, key):
	dictionary[str(key)]=None



def ProcessCSVLine(line,listOfTypes,temporaryMainItem,listIndexPosition):
	lineAsList = line.split(',')
	listIndexPosition = int(listIndexPosition)
	temporaryItem = None
	positionChange = 0
	for item in lineAsList:
		if(item ==''):
			continue
		elif(CheckRegexEquality('^\|+$',item)):
			tempItemPosition = int(listOfTypes.index(item))
			if (tempItemPosition > listIndexPosition) or (tempItemPosition < listIndexPosition):
				positionChange = listIndexPosition-tempItemPosition
				listIndexPosition = tempItemPosition
			temporaryItem = listOfTypes[listIndexPosition].copy()
			continue
		temporaryItem [listOfTypes[lineAsList.index(item)]] = ReturnStringAfter(item,'_')
	temporaryMainItem = AppendToTemporaryMain(temporaryMainItem,temporaryItem,listOfTypes,positionChange)


def AppendToTemporaryMain(mainItemAsList, temporayItem,listOfTypes,positionChange):
	var = mainItemAsList.pop()
	nItem = None
	if positionChange == 0:
		if(isinstance(var,list)):
			var.append(temporayItem)
		elif(SameTypeDictionaries(var,temporayItem)):
			var = AppendItemsIntoList(var,temporayItem)
		mainItemAsList.append(var)
	elif(positionChange <0):
		mainItemAsList.append(var)
		mainItemAsList.append(temporaryItem)
	elif(positionChange >0):
		mainItemAsList.append(var)
		List = []
		List.append(temporaryItem)
		mainItemAsList.append(List)
	return mainItemAsList


#
# Incomplete functionality
#