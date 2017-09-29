
def QuestionNineteen():
	from helper import WhileInputActive,PlaceInList
	from operator import itemgetter
	List = []
	WhileInputActive(PlaceInList,List)
	print(sorted(List,key=itemgetter(0,1,2)))

	
QuestionNineteen()

