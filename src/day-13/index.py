import os
import sys
from colorama import Fore, Style

args = sys.argv

absolute_path = os.path.dirname(os.path.abspath(__file__))
filename = absolute_path + "/input.txt"
f = open(filename,"r")

dots = []
folds = []

for line in f.readlines():
	if line.strip() == "":
		continue
	elif line.find(",") > -1:
		# we reverse the coords because our 2d arrays deal with rows first, which is in the y coordinate
		dots.append( list(map(int, reversed(line.strip().split(",")))) )
	elif line.startswith("fold"):
		folds.append( [line.split("along ")[1].split("=")[0], int(line.split("along ")[1].split("=")[1])] )

def createEmptyGrid(dots):
	xs = [i[1] for i in dots]
	ys = [i[0] for i in dots]
	x = max(xs)
	y = max(ys)
	if x % 2 != 0:
		x += 1
	if y % 2 != 0:
		y += 1
	return [ [" " for i in range(0, x + 1 )] for j in range(0, y + 1) ]

def fillGrid(grid, dots):
	for dot in dots:
		grid[dot[0]][dot[1]] = "#"
	return grid

def setLayers(layer1, layer2):
	if type(layer1[0]) == list:
		fill = [" " for i in range(0, len(layer1[0]))]
	else:
		fill = " "
	diff = [fill for i in range(0, abs(len(layer1) - len(layer2)))]
	if len(layer1) < len(layer2):
		base = diff + layer1
		overlay = layer2
	else:
		base = layer1
		overlay = layer2
	return base, overlay

def doFold(gridInput, fold):
	grid = gridInput.copy()
	if fold[0] == "x":
		for y, row in enumerate(grid):
			overlay = row[fold[1] + 1:]
			base = row[:fold[1]]
			for x, cell in enumerate(overlay):
				if cell == " ":
					continue
				base[-1 - x] = cell
			grid[y] = base
	else:
		base = grid[fold[1] + 1:]
		overlay = grid[:fold[1]]
		for y, row in enumerate(overlay):
			for x, cell in enumerate(row):
				if cell == " ":
					continue
				base[-1 - y][x] = cell
		grid = base
	return grid

def p1():
	grid = createEmptyGrid(dots)
	filledGrid = fillGrid(grid, dots)
	firstFold = doFold(filledGrid, folds[0])
	totalDots = sum([row.count("#") for row in firstFold])
	print(len(grid[0]))
	print("\n" + Style.BRIGHT + "Part 1" + Style.RESET_ALL + " Dots visible after first fold: " + Fore.YELLOW + str(totalDots) + Fore.RESET)

p1()

def p2():
	print(Style.BRIGHT + "Part 2 code:\n" + Style.RESET_ALL)
	grid = createEmptyGrid(dots)
	filledGrid = fillGrid(grid, dots)
	for fold in folds:
		filledGrid = doFold(filledGrid, fold)
	for row in reversed(filledGrid):
		print(" ".join(row))

p2()
