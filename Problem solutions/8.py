Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def QuestionEight():
	inp = input()
	processed = []
	processed = inp.split(',')
	print(','.joint(processed))

	
>>> QuestionEight()

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    QuestionEight()
  File "<pyshell#5>", line 5, in QuestionEight
    print(','.joint(processed))
AttributeError: 'str' object has no attribute 'joint'
>>> 
>>> items=[x for x in raw_input().split(',')]
items.sort()
print ','.join(items)
SyntaxError: multiple statements found while compiling a single statement
>>> items=[x for x in raw_input().split(',')]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    items=[x for x in raw_input().split(',')]
NameError: name 'raw_input' is not defined
>>> items=[x for x in input().split(',')]
Hello,World,Is,Fine
>>> items.sort()
>>> print ','.join(items)
SyntaxError: invalid syntax
>>> print (','.join(items))
Fine,Hello,Is,World
>>> 
