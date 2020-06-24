board = ["-","-","-",
		"-","-","-"
		,"-","-","-"]
game_ove = True

def display_board(board):
	print()
	print(board[0]+"|"+board[1]+"|"+board[2])
	print(board[3]+"|"+board[4]+"|"+board[5])
	print(board[6]+"|"+board[7]+"|"+board[8])
	print()
display_board(board)
current_player = "X"
#checking for a tie
def tie_game(board):
	global game_ove
	if "-" not in board:
		game_ove = False
		print("It a tie!!")
#checking for winner
def game_over(board,current_player):
	#row
	global game_ove
	if board[0] == "X" and board[1] == "X" and board[2] == "X" or (board[0] == "O" and board[1] == "O" and board[2] == "O"):
		game_ove = False
		print(current_player+" Won.")
		
	elif board[3] == "X" and board[4] == "X" and board[5] == "X" or (board[3] == "O" and board[4] == "O" and board[5] == "O"):
		game_ove = False
		print(current_player+" Won.")
	elif board[6] == "X" and board[7] == "X" and board[8] == "X" or (board[6] == "O" and board[7] == "O" and board[8] == "O"):
		game_ove = False
		print(current_player+" Won.")
	#col
	elif board[0] == "X" and board[3] == "X" and board[5] == "X" or (board[0] == "O" and board[3] == "O" and board[6] == "O"):
		game_ove = False
		print(current_player+" Won.")
	elif board[1] == "X" and board[4] == "X" and board[7] == "X" or (board[1] == "O" and board[4] == "O" and board[7] == "O"):
		game_ove = False
		print(current_player+" Won.")
	elif board[2] == "X" and board[5] == "X" and board[8] == "X" or (board[2] == "O" and board[5] == "O" and board[8] == "O"):
		game_ove = False
		print(current_player+" Won.")
	#diagonal
	elif board[0] == "X" and board[4] == "X" and board[8] == "X" or (board[0] == "O" and board[4] == "O" and board[8] == "O"):
		game_ove = False
		print(current_player+" Won.")
	elif board[2] == "X" and board[4] == "X" and board[6] == "X" or (board[2] == "O" and board[4] == "O" and board[6] == "O"):
		game_ove = False
		print(current_player+" Won.")

#playing game
while game_ove:
	print(current_player+" Turn.")
	pos = (int(input("Choose a number from 1 to 9 : "))-1)
	if "-" not in board[pos]:
		print("you cannot go in the same position!!")
		pos = (int(input("Choose a number from 1 to 9 : "))-1)
	while pos not in [0,1,2,3,4,5,6,7,8]:
		pos = int(input("Choose a number from 1 to 9 : "))
	board[int(pos)] = current_player
	display_board(board)
	game_over(board,current_player)
	tie_game(board)
	if game_ove == False:
		break
	if current_player == "X":
		current_player = "O"
	else:
		current_player = "X"
