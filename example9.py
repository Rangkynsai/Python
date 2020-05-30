lst1 = [10,20,23,11,17]
lst2 = [13,43,24,36,12]
lst3 = []
[lst3.append(i) for i in lst1 if i%2!=0]
[lst3.append(i) for i in lst2 if i%2==0]
print(lst3)