
>>> def QuestionSeven():
	X= int(input())
	Y=int(input())
	mainResult=[]
	for rows in range(X):
		newArray=[]
		for columns in range(Y):
			newArray.append(rows*columns)
		mainResult.append(newArray)
	print(mainResult);

	
>>> QuestionSeven()
