def QuestionTwelve():
	List = []
	for item in range(1000,3001):
		if (checkIfAllDigitsAreOddOrEven(item) == 'even'):
			List.append(str(item))
	print(','.join(List))

	
QuestionTwelve()