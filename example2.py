n1 = int(input('Enter the first number : '))
n2 = int(input('Enter the second number : '))
for i in range(n1,n2+1):
    print('current number : ',str(i),'previous number : ',str(i-1),'sum : ',str(i+(i+1)))