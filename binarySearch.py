def search(lst,n):
    l = 0
    u = len(lst)-1
    while l<=u:
        mid = (l+u)//2
        if lst[mid] == n:
            return True
        else:
            if lst[mid] < n:
                l = mid+1
            else:
                u = mid+1
        return False
lst = [4,7,8,12,45,99]
x = 9
if search(lst,x):
    print('Found')
else:
    print('Not Found')