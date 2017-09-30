Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s = "Hello World Hello World is fine is it ?"
>>> print(s)
Hello World Hello World is fine is it ?
>>> import zlib
>>> c = zlib.compress(s)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    c = zlib.compress(s)
TypeError: a bytes-like object is required, not 'str'
>>> c = zlib.compress(bytes(s))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    c = zlib.compress(bytes(s))
TypeError: string argument without an encoding
>>> c = zlib.compress(bytes(s),'utf-8')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    c = zlib.compress(bytes(s),'utf-8')
TypeError: string argument without an encoding
>>> help(zlib.compress)
Help on built-in function compress in module zlib:

compress(data, /, level=-1)
    Returns a bytes object containing compressed data.
    
    data
      Binary data to be compressed.
    level
      Compression level, in 0-9 or -1.

>>> c = zlib.compress(bytearray(s))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    c = zlib.compress(bytearray(s))
TypeError: string argument without an encoding
>>> c = zlib.compress(bytes(s),3)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    c = zlib.compress(bytes(s),3)
TypeError: string argument without an encoding
>>> s = s.encode('utf-'8)
SyntaxError: invalid syntax
>>> s= s.encode('utf-8')
>>> print(s)
b'Hello World Hello World is fine is it ?'
>>> c= zlib.compress(s)
>>> print(z)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(z)
NameError: name 'z' is not defined
>>> print(c)
b'x\x9c\xf3H\xcd\xc9\xc9W\x08\xcf/\xcaIQ\xf0@bg\x16+\xa4e\xe6\xa5\x82\xe8\xcc\x12\x05{\x00\x14k\ro'
>>> print(c.decompress())
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(c.decompress())
AttributeError: 'bytes' object has no attribute 'decompress'
>>> print(zlib.decompress(c))
b'Hello World Hello World is fine is it ?'
>>> s = s.decode
>>> print(s)
<built-in method decode of bytes object at 0x000001F365B85A08>

>>> s = s.decode()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s = s.decode()
AttributeError: 'builtin_function_or_method' object has no attribute 'decode'
>>> i = 'Helllo wqasd Hello'
>>> i = i.decode()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    i = i.decode()
AttributeError: 'str' object has no attribute 'decode'
>>> i = i.encode('utf-8')
>>> print(i)
b'Helllo wqasd Hello'
>>> i = i.decode()
>>> print()i
SyntaxError: invalid syntax
>>> print(i)
Helllo wqasd Hello
>>> 
