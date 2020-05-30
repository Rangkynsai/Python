lst = []
size = int(input('Enter the size of a list : '))
[lst.append(int(input('Enter the element of the list : '))) for i in range(size)]
print('----------The number are----------')
for j in lst:
    if j % 5 == 0:
        print(j)
    else:
        continue