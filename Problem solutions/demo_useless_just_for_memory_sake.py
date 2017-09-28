Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> def toDigits(n, b):
        """Convert a positive number n to its digit representation in base b."""
        digits = []
        while n > 0:
            digits.insert(0, n % b)
            n  = n // b
        return digits

>>> def fromDigits(digits, b):
        """Compute the number given by digits in base b."""
        n = 0
        for d in digits:
            n = b * n + d
        return n

>>> def convertBase(digits, b, c):
        """Convert the digits representation of a number from base b to base c."""
        return toDigits(fromDigits(digits, b), c)

>>> num = 123
>>> print(convertBase(num),10,2)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(convertBase(num),10,2)
TypeError: convertBase() missing 2 required positional arguments: 'b' and 'c'
>>> print(convertBase(num,10,2))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(convertBase(num,10,2))
  File "<pyshell#6>", line 3, in convertBase
    return toDigits(fromDigits(digits, b), c)
  File "<pyshell#4>", line 4, in fromDigits
    for d in digits:
TypeError: 'int' object is not iterable
>>> num = '123'
>>> print(convertBase(num,10,2))
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(convertBase(num,10,2))
  File "<pyshell#6>", line 3, in convertBase
    return toDigits(fromDigits(digits, b), c)
  File "<pyshell#4>", line 5, in fromDigits
    n = b * n + d
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(convertBase([1,2,3],10,2))
[1, 1, 1, 1, 0, 1, 1]
>>> def convertBase(digits, b, c):
	if(digits not list):
		digits = list(digits)
	"""Convert the digits representation of a number from base b to base c."""
	return toDigits(fromDigits(digits, b), c)
SyntaxError: invalid syntax
>>> def convertBase(digits, b, c):
	if(digits is not list):
		digits = list(digits)
	"""Convert the digits representation of a number from base b to base c."""
	return toDigits(fromDigits(digits, b), c)

>>> print(convertBase(123,10,2))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(convertBase(123,10,2))
  File "<pyshell#15>", line 3, in convertBase
    digits = list(digits)
TypeError: 'int' object is not iterable
>>> print(convertBase('123',10,2))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(convertBase('123',10,2))
  File "<pyshell#15>", line 5, in convertBase
    return toDigits(fromDigits(digits, b), c)
  File "<pyshell#4>", line 5, in fromDigits
    n = b * n + d
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> help(list)
Help on class list in module builtins:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.n
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      L.__reversed__() -- return a reverse iterator over the list
 |  
 |  __rmul__(self, value, /)
 |      Return self*value.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      L.__sizeof__() -- size of L in memory, in bytes
 |  
 |  append(...)
 |      L.append(object) -> None -- append object to end
 |  
 |  clear(...)
 |      L.clear() -> None -- remove all items from L
 |  
 |  copy(...)
 |      L.copy() -> list -- a shallow copy of L
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> print(convertBase([1,2,3],16,12))
[2, 0, 3]
>>> print(convertBase([1,2,3],16,10))
[2, 9, 1]
>>> print(convertBase([2,9,1],16,12))
[4, 6, 9]
>>> print(convertBase([2,9,1],10,16))
[1, 2, 3]
>>> print(convertBase([7,D,E],16,10))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(convertBase([7,D,E],16,10))
NameError: name 'D' is not defined
>>> print(convertBase([7,'D','E'],16,10))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(convertBase([7,'D','E'],16,10))
  File "<pyshell#15>", line 5, in convertBase
    return toDigits(fromDigits(digits, b), c)
  File "<pyshell#4>", line 5, in fromDigits
    n = b * n + d
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> i = '123'
>>> i = list(i)
>>> print(i)
['1', '2', '3']
>>> i= int(i)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    i= int(i)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> for item in i:
	item = int(item)

	
>>> print(i)
['1', '2', '3']
>>> i*2
['1', '2', '3', '1', '2', '3']
>>> j = i[0]+2
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    j = i[0]+2
TypeError: must be str, not int
>>> newI = []
>>> for item in i:
	newI.append(int(item))

	
>>> print(newI)
[1, 2, 3]
>>> def convertNumberToListOfNumbers(number):
	number = str(number)
	number=list(number)
	List = []
	for num in number:
		List.append(int(num))

		
>>> def convertNumberToListOfNumbers(number):
	number = str(number)
	number=list(number)
	List = []
	for num in number:
		List.append(int(num))
	return List

>>> print(convertNumberToListOfNumbers(123))
[1, 2, 3]
>>> List = convertNumberToListOfNumbers(123)
>>> List = str(List)
\
>>> List = str(List)
>>> print(List)
[1, 2, 3]
>>> string = ""
>>> for item in List:
	string += irem

	
Traceback (most recent call last):
  File "<pyshell#58>", line 2, in <module>
    string += irem
NameError: name 'irem' is not defined
>>> for item in List:
	string += item

	
>>> print(string)
[1, 2, 3]
>>> help(list to string)
SyntaxError: invalid syntax
>>> help()

Welcome to Python 3.6's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/3.6/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> list to str
No Python documentation found for 'list to str'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> string = ''.join(List)
>>> print(string)
[1, 2, 3]
>>> str1 = ''.join(str(e) for e in List)
>>> print(str1)
[1, 2, 3]
>>> for item in List:
	print(str(item))

	
[
1
,
 
2
,
 
3
]
>>> print (List[0])
[
>>> string = 'for'
>>> for char in string:
	print(char)

	
f
o
r
>>> def convertNumberToList(number):
	number = str(number)
	List = []
	for item in number:
		List.append(item)

		
>>> string='123'
>>> del List
>>> print(List)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    print(List)
NameError: name 'List' is not defined
>>> List=[]
>>> for item in string:
	List.append(int(item))

	
>>> print(List)
[1, 2, 3]
>>> newList = []
>>> string = ''.join(List)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    string = ''.join(List)
TypeError: sequence item 0: expected str instance, int found
>>> string = ''.join(str(item) for item in List)
>>> print(string)
123
>>> def convertNumberToList(number):
	number = str(number)
	List = []
	for item in number:
		List.append(int(item))
	return List

>>> def convertListToNumber(List):
	return int(''.join(str(item) for item in List))

>>> numberOld = 123
>>> List = convertNumberToList(numberOld)
>>> numberNew = convertListToNumber(List)
>>> print(numberNew)
123
>>> 
