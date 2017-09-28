
def QuestionSixteen():
	Input=input()
	print(",".join(str(item) for item in(Input.split(",")) if(int(item)%2!=0)))

QuestionSixteen()

