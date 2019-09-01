size = int(input('Enter the size of the list:  '))
for i in range(size):
    i = input()
    lst = list()
    lst.append(i)
target = input('Enter the element to search from the list: ')
found = False
for i in lst:
    if i == target:
        found = True
if found:
    print(f'The element {target} is found.')
