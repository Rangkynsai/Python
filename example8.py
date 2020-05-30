number = int(input('Enter a number to reverse : '))
a = number
rever = 0
while number !=0:
    remainder = number%10
    rever = (rever*10) + remainder
    number//=10
print(rever)
if rever == a:
    print('True')
else:
    print('False')