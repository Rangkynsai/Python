#creating a list
'''car_name = ['bmw','honda','ford','bugati','ducati','maruti','tesla']
#iterating throught list
for carname in car_name:
    print(carname.title()+'\n')
print('All Done!!!')
squares = []
for i in range(1,11):
    square = i**2
    squares.append(square)
print(squares)'''
#copying a list form one list to the other list using for loop
old_list = ['a','b','c','d','f']
new_list = []
for lst in old_list:
    new_list.append(lst)
print(new_list)
#finding maximum and minimum
print(max(old_list))
print(min(old_list))