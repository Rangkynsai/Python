#Guessing game
import random
r = random.randint(1,20) 
for time in range(0,10):
    guess = int(input('Guess your number : '))
    if guess < r:
        print('Your guess is low try again..')
    elif guess > r:
        print('Your guess is high try again...')
    else:
        break
if guess == r:
    print("Yay!! you got it right..")
else:
    print('Try next time.')
print('Thankyou')