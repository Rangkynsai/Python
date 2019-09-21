#Enter the size of the list
size = int(input('Enter the size of the list: '))
lst = []
for i in range(size):
    i = int(input(f'Enter the {size} element: '))
    lst.append(i)
target = int(input('Enter the number to search: '))
bol = False
for j in lst:
    if j == target:
        bol = True
        break
    else:
        bol = False
if bol:
    print(f'The number {target} is found in the list. :')
else:
    print(f'The number {target} is not found in the list.')
print('Thankyou!!')