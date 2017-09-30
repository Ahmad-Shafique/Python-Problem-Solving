Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class MyError(Exception):
    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg

>>> error = MyError("something wrong")
>>> raise MyError
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    raise MyError
TypeError: __init__() missing 1 required positional argument: 'msg'
>>> x = MyError()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x = MyError()
TypeError: __init__() missing 1 required positional argument: 'msg'
>>> raise x.MyError()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    raise x.MyError()
NameError: name 'x' is not defined
>>> def samp():
	try:
		print(5/0)
	except Exception:
		raise MyError

	
>>> samp()
Traceback (most recent call last):
  File "<pyshell#10>", line 3, in samp
    print(5/0)
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    samp()
  File "<pyshell#10>", line 5, in samp
    raise MyError
TypeError: __init__() missing 1 required positional argument: 'msg'
>>> class a:
	pass

>>> b = a()
>>> raise b.MyError()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    raise b.MyError()
AttributeError: 'a' object has no attribute 'MyError'
>>> raise MyError('My error')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    raise MyError('My error')
MyError: My error
>>> 
