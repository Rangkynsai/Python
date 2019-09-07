n = int(input('Number of command: '))
lst = []
for i in range(n):
    str1 = input('Command: ')
    if str1 == 'insert':
        position = int(input('Enter the position: '))
        value =int(input('Value: '))
        lst.insert(position,value)  
    elif str1 == 'remove':
        value =int(input('Value: '))
        lst.remove(value)
    elif str1 == 'append':
        value =int(input('Value: '))
        lst.append(value)
    elif str1 == 'sort':
        lst.sort()
    elif str1 == 'pop':
        lst.pop()
    elif str1 == 'reverse':
        lst.reverse()
    elif str1 == 'print':
        print(lst)