Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup = tuple([1,2,3,4,5,6,7,8,9,10])
>>> print(tup)
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
>>> l = len(tuple)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    l = len(tuple)
TypeError: object of type 'type' has no len()
>>> l = len(tup)
>>> print(",".join(str(item) for item in tup[:l/2]))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(",".join(str(item) for item in tup[:l/2]))
TypeError: slice indices must be integers or None or have an __index__ method
>>> hl = l/2
>>> print(",".join(str(item) for item in tup[:hl]))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(",".join(str(item) for item in tup[:hl]))
TypeError: slice indices must be integers or None or have an __index__ method
>>> print(tup[:hl])
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(tup[:hl])
TypeError: slice indices must be integers or None or have an __index__ method
>>> print(tup[:int(hl)])
(1, 2, 3, 4, 5)
>>> print(",".join(str(item) for item in tup[:int(hl)]))
1,2,3,4,5
>>> print(",".join(str(item) for item in tup[int(hl):]))
6,7,8,9,10
>>> 
