Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def QuestionEighteen():
	Input = input();
	List = []
	List = Input.split(",")
	import re
	for item in List:
		if not (re.search('^(?=.{6,12})(?=.*[a-z]+)(?=.*[A-Z]+)(?=.*[0-9]+)(?=.*[$#@]+).{6,12}$',item)):
			List.remove(item)
	print(",".join(List))

	
>>> QuestionEighteen()
ABd1234@1,a F1#,2w3E*,2We3345
ABd1234@1,2w3E*
>>> Input = input()
ABd1234@1,a F1#,2w3E*,2We3345
>>> List = []
>>> List = Input.split(",")
>>> print(List)
['ABd1234@1', 'a F1#', '2w3E*', '2We3345']
>>> def QuestionEighteen():
	Input = input();
	List = []
	List = Input.split(",")
	import re
	Result = []
	for item in List:
		if (re.search('^(?=.{6,12})(?=.*[a-z]+)(?=.*[A-Z]+)(?=.*[0-9]+)(?=.*[$#@]+).{6,12}$',item)):
			Result.append(item)
	print(",".join(Result))

	
>>> QuestionEighteen()
ABd1234@1,a F1#,2w3E*,2We3345
ABd1234@1
>>> 
