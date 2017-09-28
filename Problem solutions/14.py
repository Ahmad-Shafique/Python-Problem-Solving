Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> i='adsfasdfASDDsfsda'
>>> for item in i:
	    if(item.isupper()):
		    print (item)

		    
A
S
D
D
>>> def checkNumberOfUpperCaseLetters(string):
	number = 0
	for item in i:
	    if(item.isupper()):
		    number +=1
	return number

>>> def checkNumberOfLowerCaseLetters(string):
	number = 0
	for item in i:
	    if(item.islower()):
		    number +=1
	return int(number)

>>> print(checkNumberOfLowerCaseLetters(i))
13
>>> print(checkNumberOfUpperCaseLetters(i))
4
>>> def QuestionFourteen():
	Input = input();
	print('Upper Case : '+str(checkNumberOfUpperCaseLetters(Input)))
	print('Lower Case : '+str(checkNumberOfLowerCaseLetters(Input)))

	
>>> QuestionFourteen()
Hello world!
Upper Case : 4
Lower Case : 13
>>> 
