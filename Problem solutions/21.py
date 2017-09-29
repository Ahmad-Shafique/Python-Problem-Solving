Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def QuestionTwentyOne():
	robotXAxis = 0;
	robotYAxis = 0;

	
>>> 
>>> from helper import WhileInputActive,PlaceInList
>>> list = []
>>> WhileInputActive(PlaceInList, list)
UP 5
DOWN 3
LEFT 3
RIGHT 2

>>> x=0
>>> y=0
>>> for item in list:
	nl = item.split(" ")
	if(nl[0] == 'UP'):

	elif(nl[0] == 'DOWN'):
		
SyntaxError: expected an indented block
>>> for item in list:
	nl = item.split(" ")
	if(nl[0] == 'UP'):

	elif(nl[0] == 'DOWN'):
		
SyntaxError: expected an indented block
>>> for item in list:
	nl = item.split(" ")
	if(nl[0] == 'UP'):
		y += int(nl[1])
	elif(nl[0] == 'DOWN'):
		y -= int(nl[1])
	elif(nl[0] == 'LEFT'):
		x -= int(nl[1])
	elif(nl[0] == 'RIGHT'):
		x += int(nl[1])

		
>>> from math import sqrt
>>> dist = sqrt(((1-x)^2) + ((1-y)^2))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    dist = sqrt(((1-x)^2) + ((1-y)^2))
ValueError: math domain error
>>> dist = sqrt(((1-x)^2) + ((1-y)^2)))
SyntaxError: invalid syntax
>>> dist = sqrt(float((1-x)^2) + float((1-y)^2))
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    dist = sqrt(float((1-x)^2) + float((1-y)^2))
ValueError: math domain error
>>> import math
>>> dist = math.sqrt(float((1-x)^2) + float((1-y)^2))
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    dist = math.sqrt(float((1-x)^2) + float((1-y)^2))
ValueError: math domain error
>>> print(sqrt(4))
2.0
>>> print(sqrt(float((1-2)^2) + float((1-2)^2)))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(sqrt(float((1-2)^2) + float((1-2)^2)))
ValueError: math domain error
>>> print(sqrt(float((1-2)^2)))
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(sqrt(float((1-2)^2)))
ValueError: math domain error
>>> print(sqrt(float((1-2)^2))))
SyntaxError: invalid syntax
>>> print(sqrt(float((1-2)^2)))
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(sqrt(float((1-2)^2)))
ValueError: math domain error
>>> xdif = (1-x)^2
>>> ydif = (1-y)^2
>>> dist = sqrt(xdif+ydif)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    dist = sqrt(xdif+ydif)
ValueError: math domain error
>>> tot = xdif+ydif
>>> print(sqrt(tot))
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(sqrt(tot))
ValueError: math domain error
>>> print(sqrt(int(tot)))
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print(sqrt(int(tot)))
ValueError: math domain error
>>> print(tot)
-3
>>> tot = -tot
>>> print(sqrt(tot))
1.7320508075688772
>>> 
