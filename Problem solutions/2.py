
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)


while True:
	i=input()
	if (i!='\n'):
		i=int(i)
		print(fact(i),end=',')
	else:
		break

		
