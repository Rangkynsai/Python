def search(lst,x):
    for i in lst :
        if i == x:
            return True
    return False

lst = [5,8,4,6,9,2]

Target = 10

if search(lst,Target):
    print('Found')
else:
    print('Not found')