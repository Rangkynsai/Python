birthday = {'alice' : 'Apr 1','bob':'Dec 12','Carol':'Mar 4'}
while True:
    print('Enter a name : (blank to quit)')
    name = input()
    if name =='':
        break
    if name in birthday:
        print(birthday[name]+' is the birthday of '+name)
    else:
        print('I do not have a birthday iinformation for '+name)
        bday = input('What is their birthday ?')
        birthday[name] = bday
        print('Birthday database updated.')