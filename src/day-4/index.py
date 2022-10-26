import os
import sys

args = sys.argv
print(args)

absolute_path = os.path.dirname(os.path.abspath(__file__))
filename = absolute_path + "/input.txt"
f = open(filename,"r")
lines = f.readlines()

calls = lines[0].strip().split(',')

boardsRaw = lines
boardsRaw.pop(0)
boards = []
boardTemp = []
for line in boardsRaw:
	if line.strip() == '':
		if len(boardTemp) > 0:
			boards.append(boardTemp)
		boardTemp = []
	else:
		boardTemp.append(line.strip().split())

boardRows = len(boards[0])
boardCols = len(boards[0][0])

def getBoard(board):
	board = boards[board]
	return board

lastNumber = 0

def checkMatch():
	number = lastNumber
	for b in range(len(boards)):
		for r in range(len(boards[b])):
			for c in range(len(boards[b][r])):
				if boards[b][r][c] == number:
					boards[b][r][c] = 'x'
					# print('Matched ' + str(number) + ' to ' + str(r) + ',' + str(c) + ' on board ' + str(b))
					break

def isSubset(superset, subset):
	return all(item in superset for item in subset)

winningBoards = []
winningBoard = -1

def checkWin(b):
	if b in winningBoards:
		return False
	for row in boards[b]:
		if all(cell == 'x' for cell in row):
			print('Board ' + str(b) + ' is a winner!')
			return True
		else:
			for c in range(boardCols):
				if all(boards[b][r][c] == 'x' for r in range(boardRows)):
					print('Board ' + str(b) + ' is a winner!')
					return True
	return False

def getUnmarked(b):
	unmarked = []
	for row in boards[b]:
		for cell in row:
			if cell != 'x':
				unmarked.append(int(cell))
	return unmarked

def getScore(unmarked):
	return sum(unmarked) * int(lastNumber)



if 'last' in args:
	while len(winningBoards) < len(boards) and len(calls) > 0:
		lastNumber = calls[0]
		checkMatch()
		for b in range(len(boards)):
			isWinner = checkWin(b)
			if isWinner:
				winingBoard = b
				winningBoards.append(b)
		calls.pop(0)
else:
	while len(winningBoards) < 1 and len(calls) > 0:
		lastNumber = calls[0]
		checkMatch()
		for b in range(len(boards)):
			isWinner = checkWin(b)
			if isWinner:
				winingBoard = b
				winningBoards.append(b)
		calls.pop(0)

print(winningBoards)
winningBoard = winningBoards[len(winningBoards) - 1]
winner = getBoard(winningBoard)
print('Winning board:', winningBoard)
for row in winner:
	print(row)

# Get board score
unmarked = getUnmarked(winningBoard)
score = getScore(unmarked)

print('Winning board:', winningBoard)
print('Unmarked numbers:', unmarked, 'Sum:', sum(unmarked))
print('Last number drawn: ', lastNumber)
print('Score: ', str(score))
