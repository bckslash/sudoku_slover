import os

board_hardest = [
		[8, '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', 3, 6, '*', '*', '*', '*', '*'],
		['*', 7, '*', '*', 9, '*', 2, '*', '*'],
		['*', 5, '*', '*', '*', 7, '*', '*', '*'],
		['*', '*', '*', '*', 4, 5, 7, '*', '*'],
		['*', '*', '*', 1, '*', '*', '*', 3, '*'],
		['*', '*', 1, '*', '*', '*', '*', 6, 8],
		['*', '*', 8, 5, '*', '*', '*', 1, '*'],
		['*', 9, '*', '*', '*', '*', 4, '*', '*']
		]

board_miracle = [
		['*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', 4, '*', '*', '*', '*'],
		['*', '*', 3, '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*'],
		['*', '*', '*', '*', '*', '*', '*', '*', '*']
		]

def clear(): 
	os.system('cls' if os.name == 'nt' else 'clear')

def solve(board):

	# draw_board(board)
	# clear()
	find = find_empty(board)
	if not find:
		return True
	else:
		row, col = find

	for i in range(1, 10):
		if valid(board, i, (row, col)):
			board[row][col] = i

			if solve(board):
				return True

			board[row][col] = 0

	return False

def valid(board, num, pos):
	#check row
	for i in range(len(board[0])):
		if board[pos[0]][i] == num and pos[1] != i:
			return False

	#check col
	for i in range(len(board)):
		if board[i][pos[1]] == num and pos[0] != i:
			return False

	#check box
	box_x = pos[1] // 3
	box_y = pos[0] // 3

	for i in range(box_y * 3, box_y*3 + 3):
		for j in range(box_x * 3, box_x*3 + 3):
			if board[i][j] == num and (i, j) != pos:
				return False

	return True

def draw_board(board):

	for i in range(len(board)):
		if i % 3 == 0 and i != 0:
			print("---------------------")

		for j in range(len(board[0])):
			if j % 3 == 0 and j != 0:
				print("| ", end="")

			if j == 8:
				print(board[i][j])

			else:
				print(str(board[i][j]) + " ", end="")

def find_empty(board):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j] == '*':
				return (i, j) #row, col

	return None

board = board_hardest

clear()
draw_board(board)
input("Press Enter to solve...\n")
solve(board)
print("DONE!")
draw_board(board)