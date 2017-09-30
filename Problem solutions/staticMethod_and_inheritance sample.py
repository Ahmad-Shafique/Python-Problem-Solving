Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> help(map)
Help on class map in module builtins:

class map(object)
 |  map(func, *iterables) --> map object
 |  
 |  Make an iterator that computes the function using arguments from
 |  each of the iterables.  Stops when the shortest iterable is exhausted.
 |  
 |  Methods defined here:
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __next__(self, /)
 |      Implement next(self).
 |  
 |  __reduce__(...)
 |      Return state information for pickling.

>>> class a:
	def xyz():
		print('xyz');

		
>>> a.xyz()
xyz
>>> class b:
	@staticmethod
	def abc():
		print("abc");

	
>>> b.abc()
abc
>>> class c(a,b):
	pass

>>> print(c.xyz())
xyz
None
>>> print(c)
<class '__main__.c'>
>>> print(c.abc)
<function b.abc at 0x0000026850AC6048>
>>> print(c.abc())
abc
None
>>> class d(a):
	def xyz():
		print('newXyz')

		
>>> print(d.xyz())
newXyz
None
>>> dN = d()
>>> print(dN.xyz())
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(dN.xyz())
TypeError: xyz() takes 0 positional arguments but 1 was given
>>> 
