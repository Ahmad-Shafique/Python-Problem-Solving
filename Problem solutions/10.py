def QuestionTen():
	Input = input();
	listFromInput = Input.split(" ");
	listFromInput = sorted(set(listFromInput))
	print(listFromInput);


QuestionTen();
