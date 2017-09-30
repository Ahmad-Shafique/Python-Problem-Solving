Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def TryCatchSample():
	inp = Input()
	try:
		print(inp+5)
	except TypeError as typ:
		print("Type Error: ",typ)
	except ZeroDivisionError as zre:
		print("ZDE: ",zre)
	else:
		print('some error raised during execution... function failure !')
	finally:
		print("Function end");

		
>>> TryCatchSample()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    TryCatchSample()
  File "<pyshell#13>", line 2, in TryCatchSample
    inp = Input()
NameError: name 'Input' is not defined
>>> def TryCatchSample():
	try:
		inp = Input()
		print(inp+5)
	except TypeError as typ:
		print("Type Error: ",typ)
	except ZeroDivisionError as zre:
		print("ZDE: ",zre)
	else:
		print('some error raised during execution... function failure !')
	finally:
		print("Function end");

		
>>> TryCatchSample()
Function end
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    TryCatchSample()
  File "<pyshell#16>", line 3, in TryCatchSample
    inp = Input()
NameError: name 'Input' is not defined
>>> def TryCatchSample():
	try:
		inp = Input()
		print(inp+5)
	except TypeError as typ:
		print("Type Error: ",typ)
	except ZeroDivisionError as zre:
		print("ZDE: ",zre)
	except Exception as exc:
		print("An exception found: ",exc)
	else:
		print('some error raised during execution... function failure !')
	finally:
		print("Function end");

		
>>> TryCatchSample()
An exception found:  name 'Input' is not defined
Function end
>>> def TryCatchSample():
	try:
		inp = input()
		print(inp+5)
	except TypeError as typ:
		print("Type Error: ",typ)
	except ZeroDivisionError as zre:
		print("ZDE: ",zre)
	except Exception as exc:
		print("An exception found: ",exc)
	else:
		print('some error raised during execution... function failure !')
	finally:
		print("Function end");

		
>>> TryCatchSample()
asdf
Type Error:  must be str, not int
Function end
>>> TryCatchSample()
10
Type Error:  must be str, not int
Function end
>>> TryCatchSample()
'asd'
Type Error:  must be str, not int
Function end
>>> def TryCatchSample():
	try:
		inp = input()
		print(int(inp)+5)
	except TypeError as typ:
		print("Type Error: ",typ)
	except ZeroDivisionError as zre:
		print("ZDE: ",zre)
	except Exception as exc:
		print("An exception found: ",exc)
	else:
		print('some error raised during execution... function failure !')
	finally:
		print("Function end");

		
>>> TryCatchSample()
asd
An exception found:  invalid literal for int() with base 10: 'asd'
Function end
>>> TryCatchSample()
10
15
some error raised during execution... function failure !
Function end
>>> TryCatchSample()
dsfa
An exception found:  invalid literal for int() with base 10: 'dsfa'
Function end
>>> 
