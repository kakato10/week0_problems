def prepare_meal(number):
	meal=''
	t=0
	if number%3==0:
		for i in range (1,number):
			if 3**i>number:
				break
			if number%(3**i)==0:
				t=t+1
	meal=meal+ ('spam ' * t)
	if number%5==0:
		if number%(3**t)==0 and t>0:
			meal= meal + ('and eggs')
		else:
		 meal= meal + "eggs"
	return meal
