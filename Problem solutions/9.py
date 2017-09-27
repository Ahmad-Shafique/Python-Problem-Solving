Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import helper
>>> def QuestionNine():
	listOfInput = [];
	helper.WhileInputActive(helper.PlaceInList,listOfInput)
	for item in listOfInput:
		print(item.upper());

		
>>> QuestionNine()
Hello World
How are you ?

HELLO WORLD
HOW ARE YOU ?
>>> 
