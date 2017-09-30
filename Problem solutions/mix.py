Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Subject = ['I','You']
>>> Verb =['Play','Love']
>>> Object = ['Hockey','Football']
>>> Sentences = []
>>> for s in Subject:
	for v in Verb:
		for o in Object:
			Sentences.append(s + " " +v + " " + o)

>>> for item in Sentences:
	print(item)

	
I Play Hockey
I Play Football
I Love Hockey
I Love Football
You Play Hockey
You Play Football
You Love Hockey
You Love Football
>>> 
