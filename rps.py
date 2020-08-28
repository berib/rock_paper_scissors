from random import randint

# List of play options
t = ['Rock', 'Paper', 'Scissors']

def computer():
	"""Randomly chooses an item from the t list

	Parameters
	----------
	none

	Retuns
	------
	a random item from the t list
	"""
	f = t[randint(0,2)]
	return f

def player():
	"""Player input inside  a while loop to catch non int errors

	Parameters
	----------
	none

	Returns 
	-------
	An item from the game list the player chose
	"""
	while True:
		try:
			choice = int(input('1.Rock, 2.Paper, 3.Scissors'))
			return t[choice-1]
			break
		except:
			print('Pick a number from 1 to 3')	

def winner(computer,player):
	"""Checks if there is a tie or winner

	Parameters
	----------
	computer: Computer's random choice
	player: Player's choice

	Returns
	-------
	nothing, it just prints who won, if there is a winner, prints tie otherwise
	"""
	if player == computer:
		print('Tie')
	elif player == 'Rock'	and computer == 'Scissors':
		print(f"Player wins with {player} over {computer}")
	elif player == 'Scissors' and computer == "Paper":
		print(f"Player wins with {player} over {computer}")
	elif player == 'Paper' and computer == 'Rock':
		print(f"Player wins with {player} over {computer}")

	else:
		print(f"Computer wins with {computer} over {player}")	
			





def game():
	"""Runs player() and computer() and compares them with the winner()

	Parameters
	----------
	none

	Returns
	-------
	nothing
	""" 
	com = computer()
	pla = player()
	print (f'You chose {pla}')
	print(f"Computer choose {com}")

	winner(com,pla)

game_on = True

# Game loop
while game_on:
	play_again = True
	game()
	# Play again or not loop
	while play_again:
		sk = input('Wanna play again? Y/N')
		if sk.lower() == 'y':
			break
		elif sk.lower() == 'n':
			play_again=False
			game_on=False
		else:
			print('Please, type Y or N')		