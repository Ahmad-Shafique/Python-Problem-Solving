def WhileInputActive(function,List=None):
        while True:
                inputVariable = input();
                if (inputVariable is None) or (not inputVariable):
                        break;
                if (List is None):
                        function(inputVariable);
                else:
                        function(List,inputVariable);



def PlaceInList(List,Input):
	List.append(Input);
		

