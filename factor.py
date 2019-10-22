x = int(input("Enter the integer :"))
position = int(input("Enter the pth: "))

def factor_of(x,p):
    lst = []
    for i in range(1,x+1):
        if x % i == 0:
            lst.append(i)
    #print(lst)
    if p == 3:
        return lst[p]
    else:
        return 0

print(factor_of(x,position))