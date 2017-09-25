class StringGetPrint:
	def getString(self):
		self.string = input();
	def printString(self):
		print(self.string.upper());

		
def QuestionFive():
	stringGetPrint = StringGetPrint();
	stringGetPrint.getString();
	stringGetPrint.printString();

	
QuestionFive();
