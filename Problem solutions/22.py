Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> inp = input()
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3
>>> list = []
>>> list = inp.split(" ")
>>> d = dict()
>>> for item in list:
	if(dict[item] is None):
		dict[item] = 1
	else:
		dict[item] += 1

		
Traceback (most recent call last):
  File "<pyshell#9>", line 2, in <module>
    if(dict[item] is None):
TypeError: 'type' object is not subscriptable
>>> print(list)
['New', 'to', 'Python', 'or', 'choosing', 'between', 'Python', '2', 'and', 'Python', '3?', 'Read', 'Python', '2', 'or', 'Python', '3']
>>> d = dict(list)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d = dict(list)
ValueError: dictionary update sequence element #0 has length 3; 2 is required
>>> d.update(list)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    d.update(list)
ValueError: dictionary update sequence element #0 has length 3; 2 is required
>>> del d
>>> d = dict(list)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d = dict(list)
ValueError: dictionary update sequence element #0 has length 3; 2 is required
>>> d = dict()
>>> for item in list:
	d[item] = 1

	
>>> print(d)
{'New': 1, 'to': 1, 'Python': 1, 'or': 1, 'choosing': 1, 'between': 1, '2': 1, 'and': 1, '3?': 1, 'Read': 1, '3': 1}
>>> del d
>>> d = dict()
>>> help(dict)
Help on class dict in module builtins:

class dict(object)
 |  dict() -> new empty dictionary
 |  dict(mapping) -> new dictionary initialized from a mapping object's
 |      (key, value) pairs
 |  dict(iterable) -> new dictionary initialized as if via:
 |      d = {}
 |      for k, v in iterable:
 |          d[k] = v
 |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
 |      in the keyword argument list.  For example:  dict(one=1, two=2)
 |  
 |  Methods defined here:
 |  
 |  __contains__(self, key, /)
 |      True if D has a key k, else False.
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
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |  
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Returns a new dict with keys from iterable and values equal to value.
 |  
 |  get(...)
 |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |  
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |  
 |  setdefault(...)
 |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> for item in list:
	if(d.contains(item)):
		d[item] += 1
	else:
		d[item] = 1

		
Traceback (most recent call last):
  File "<pyshell#28>", line 2, in <module>
    if(d.contains(item)):
AttributeError: 'dict' object has no attribute 'contains'
>>> for item in list:
	if item in d:
		d[item] += 1
	else:
		d[item] = 1

		
>>> print(d)
{'New': 1, 'to': 1, 'Python': 5, 'or': 2, 'choosing': 1, 'between': 1, '2': 2, 'and': 1, '3?': 1, 'Read': 1, '3': 1}
>>> print(d.split("'"))
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(d.split("'"))
AttributeError: 'dict' object has no attribute 'split'
>>> print(d.split(","))
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(d.split(","))
AttributeError: 'dict' object has no attribute 'split'
>>> for item in d:
	print(str(item))

	
New
to
Python
or
choosing
between
2
and
3?
Read
3
>>> for item in d:
	print(str(item) + str(d[item]))

	
New1
to1
Python5
or2
choosing1
between1
22
and1
3?1
Read1
31
>>> for item in d:
	print(str(item) +" : "+ str(d[item]))

	
New : 1
to : 1
Python : 5
or : 2
choosing : 1
between : 1
2 : 2
and : 1
3? : 1
Read : 1
3 : 1
>>> 
