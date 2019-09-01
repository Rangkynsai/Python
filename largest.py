def find_len(list):
    length=len(list)
    list.sort()
    print(list[length-2])
    print(list[1])
list=[4,3,2,2,1,5,6,7]
larg=find_len(list)