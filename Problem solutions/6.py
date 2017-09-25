def QuestionSix():
	import math;
	C=50;
	H=30;
	D=input();
	inputList = []
	result = []
	inputList = D.split(',');
	for item in inputList:
		Q = math.sqrt((2*C*int(item))/H);
		result.append(str(Q));
	print(','.join(result));

	
QuestionSix()