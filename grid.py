'''
+ - - - - + - - - - + 
|         |         | 
|         |         | 
|         |         | 
|         |         | 
+ - - - - + - - - - + 
|         |         | 
|         |         | 
|         |         | 
|         |         | 
+ - - - - + - - - - + 
'''
ls = co = 10
for row in range(ls+1):
	for col in range(co+1):
		if row == 0 or row == ls//2 or row == ls:
			if col == 0 or col == co//2 or col == co:
				print("+",end= " ")
			else:
				print("-",end = " ")
		else:
			if col == 0 or col == co//2 or col == co:
				print("|",end= " ")
			else:
				print(" ",end=" ")
	print()
			
