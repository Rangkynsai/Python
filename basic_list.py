#creating a list
'''name = ['a','b','c','d','e','f','g']
message = 'Hello '+ name[5] + '.'
print(message)
#modify the list using append,insert,pop,remove function
#creating a list
car_name = ['BMW','HONDA','LAMBORGINI','AUDI','BUGATI']
#adding an element to the list
car_name.append('MARUTI')
car_name.append('TESLA')
print('\n')
print('The old item in a list are:\n',car_name)
print('\n')
#inserting an element to a particular position
car_name.insert(3,'DUCATI')
car_name.insert(4,'FORD')
print('After inserting some new item in a list:\n',car_name)
#copying a list to the other list
new_list = car_name
print('\n')
print('The new item in a list are:\n', new_list)
#deleting an element from a list
del new_list[3]
print(new_list)
#pop the elment from the list
pop_value = car_name.pop()
print('After poping the last item:\n',car_name)
print(pop_value)
print('\n')
print(car_name.pop(3))
print(car_name.pop(5))
print(car_name)
#remove is use for deleting an element by value
print(car_name.remove('BMW'))
print(car_name.remove('BUGATI'))
print(car_name)
print(new_list)
print('\n')
#sorting the list, it will sort the list alphabetical order
car_name.sort()
print(car_name)
print(new_list)
#sorting in reverse
car_name.sort(reverse = True)
print(car_name,new_list)'''
lst = [5, 10, 9, 1]
lst.sort()
print(lst)