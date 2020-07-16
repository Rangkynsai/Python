import random
def play(player,arr):
    opponent = random.choice(arr)
    if player == 'r' and opponent == 's' or (player == 's' and opponent == 'r') or (player == 'p' and opponent == 's'):
        return 'You won!'
    elif player == opponent:
        return 'It a tie!'
    else:
        return 'You lost!'
player = input('r:rock , p:paper , s:scissor \n')
arr = ['r','p','s']
print(play(player,arr))
