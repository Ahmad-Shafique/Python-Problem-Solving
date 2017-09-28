def QuestionEleven():
	Input=input()
	List = Input.split(",")
	resultList = []
	for item in List:
		ni=item
		if(number_conversion_helper.convertToBase(ni,2,10)%5==0):
			resultList.append(item)
	print(",".join(resultList))

	
QuestionEleven()
