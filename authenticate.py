def authentication(userId,password):
    if userId == 'example@gmail.com' and password == 'python@example':
        print('Login succesful!!')
    else:
        print('Invalid User Name or Password')


print('Welcome to the python world')

user_name = input('User Name:  ')

password = input('Password:  ')

authentication(user_name,password)