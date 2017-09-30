Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class a:
	def A():
		print('A')
	def A(self):
		raise RuntimeError('The function  is only defined as static')

	
>>> print(a.A())
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(a.A())
TypeError: A() missing 1 required positional argument: 'self'
>>> A = a()
>>> print(A.A())
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(A.A())
  File "<pyshell#5>", line 5, in A
    raise RuntimeError('The function  is only defined as static')
RuntimeError: The function  is only defined as static
>>> 
