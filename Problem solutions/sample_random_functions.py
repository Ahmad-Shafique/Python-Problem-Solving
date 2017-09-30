Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from random import random
>>> from random import random,sample
>>> from random import random,sample,randrange
>>> a = random()
>>> b = sample(6)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    b = sample(6)
TypeError: sample() missing 1 required positional argument: 'k'
>>> b = sample([i if i%2==0],3)
SyntaxError: invalid syntax
>>> b= sample([i for i in range(2,6)],2)
>>> c = sample([i for i in range(1000,2000) if i%2 == 0],10)
>>> d = randrange(1,3)
>>> print(a)
0.9088894105808746
>>> print(",".join(str(i) for  i in b))
3,5
>>> print(",".join(str(i) for  i in c))
1766,1704,1170,1964,1238,1296,1820,1806,1058,1640
>>> print(d)
1
>>> 
