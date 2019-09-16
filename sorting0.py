n = int(input('Enter the size: '))
lst = []
for i in range(n):
    i = int(input("Enter the element: "))
    lst.append(i)
print('Before sorting')
print(lst)
for i in range(0,n,1):
    for j in range(i+1,n-1,1):
        if lst[i] > lst [j]:
            temp = lst[i]
            lst[i] =lst[j]
            lst[j] = temp
print('After sorting')
print(lst)