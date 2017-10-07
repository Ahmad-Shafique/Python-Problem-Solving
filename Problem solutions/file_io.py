Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> with ('someFile.txt') as file:
	print('something')

	
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    with ('someFile.txt') as file:
AttributeError: __enter__
>>> with open('testFile.txt') as file:
	datta =file.read();
	print(datta)

	
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    with open('testFile.txt') as file:
FileNotFoundError: [Errno 2] No such file or directory: 'testFile.txt'
>>> C:\Users\Redoubt\Desktop\Python practice\Problem solutions
SyntaxError: unexpected character after line continuation character
>>> with open('C:\\Users\\Redoubt\\Desktop\\Python practice\\Problem solutions\\testFile.txt') as file:
	datta =file.read();
	print(datta)

	
Inside file line 1

>>> with open('C:\\Users\\Redoubt\\Desktop\\Python practice\\Problem solutions\\testFile.txt') as file:
	datta =file.read();
	print(datta)

	
Inside file line 1
Inside file line 2
Inside file line 3
1
2
3


>>> with open('C:\\Users\\Redoubt\\Desktop\\Python practice\\Problem solutions\\testFile.txt') as file:
	datta =file.readline();
	print(datta)

	
Inside file line 1

>>> with open('C:\\Users\\Redoubt\\Desktop\\Python practice\\Problem solutions\\testFile.txt') as file:
	for item in file.read()
		print(item)
		
SyntaxError: invalid syntax
>>> with open('C:\\Users\\Redoubt\\Desktop\\Python practice\\Problem solutions\\testFile.txt') as file:
	for item in file.read():
		print(item)

		
I
n
s
i
d
e
 
f
i
l
e
 
l
i
n
e
 
1


I
n
s
i
d
e
 
f
i
l
e
 
l
i
n
e
 
2


I
n
s
i
d
e
 
f
i
l
e
 
l
i
n
e
 
3


1


2


3




>>> with open('C:\\Users\\Redoubt\\Desktop\\Python practice\\Problem solutions\\testFile.txt') as file:
	for item in file.readline():
		print(item)

		
I
n
s
i
d
e
 
f
i
l
e
 
l
i
n
e
 
1


>>> file.write('Written from program')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    file.write('Written from program')
ValueError: I/O operation on closed file.
>>> with open('C:\\Users\\Redoubt\\Desktop\\Python practice\\Problem solutions\\testFile.txt') as file:
	file.write('Written from interpreter')
	for item in file.readline():
		print(item)

		
Traceback (most recent call last):
  File "<pyshell#21>", line 2, in <module>
    file.write('Written from interpreter')
io.UnsupportedOperation: not writable
>>> with open('C:\\Users\\Redoubt\\Desktop\\Python practice\\Problem solutions\\testFile.txt') as file:
	file.write('Written from interpreter')

	
Traceback (most recent call last):
  File "<pyshell#23>", line 2, in <module>
    file.write('Written from interpreter')
io.UnsupportedOperation: not writable
>>> with open('C:\\Users\\Redoubt\\Desktop\\Python practice\\Problem solutions\\testFile.txt', 'r+') as file:
	file.write('Written from interpreter')
	for item in file.readline():
		print(item)

		
24
I
n
s
i
d
e
 
f
i
l
e
 
l
i
n
e
 
1


>>> with open('C:\\Users\\Redoubt\\Desktop\\Python practice\\Problem solutions\\testFile.txt', 'r+') as file:
	for item in file.readline():
		print(item)

		
I
n
s
i
d
e
 
f
i
l
e
 
l
i
n
e
 
1


>>> with open('C:\\Users\\Redoubt\\Desktop\\Python practice\\Problem solutions\\testFile.txt', 'r+') as file:
	file.write('New from interpreter')
	for item in file.read():
		print(item)

		
20
I
n
s
i
d
e
 
f
i
l
e
 
l
i
n
e
 
2


I
n
s
i
d
e
 
f
i
l
e
 
l
i
n
e
 
3


1


2


3




W
r
i
t
t
e
n
 
f
r
o
m
 
i
n
t
e
r
p
r
e
t
e
r
>>> 
