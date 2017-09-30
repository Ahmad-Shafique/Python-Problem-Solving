Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> li = [1,2,3,4]
>>> print(",".join(str(item) for item in shuffle(li)))
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(",".join(str(item) for item in shuffle(li)))
NameError: name 'shuffle' is not defined
>>> li = shuffle(li)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    li = shuffle(li)
NameError: name 'shuffle' is not defined
>>> shuffle(li)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    shuffle(li)
NameError: name 'shuffle' is not defined
>>> from random import shuffle
>>> print(",".join(str(item) for item in shuffle(li)))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(",".join(str(item) for item in shuffle(li)))
TypeError: 'NoneType' object is not iterable
.
>>> shuffle(li)
>>> print(",".join(str(item) for item in li))
4,2,1,3
>>> 
