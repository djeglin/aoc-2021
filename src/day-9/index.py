import os
import sys
from functools import reduce

args = sys.argv

absolute_path = os.path.dirname(os.path.abspath(__file__))
filename = absolute_path + "/input.txt"
f = open(filename,"r")
lines = f.readlines()
heightmap = [list(line.strip()) for line in lines]

def checkVerticalsAreLarger(coords):
	row = coords[0]
	col = coords[1]
	cols = len(heightmap[0]) - 1
	rows = len(heightmap) - 1
	above = False
	below = False
	if row == 0:
		above = True
	elif heightmap[row][col] < heightmap[row - 1][col]:
		above = True
	if row == rows:
		below = True
	elif heightmap[row][col] < heightmap[row + 1][col]:
		below = True
	return above and below

def getLowSpots():
	lowSpotIndexes = []
	rl = len(heightmap[0]) - 1
	cl = len(heightmap) - 1
	for r, row in enumerate(heightmap):
		for c, col in enumerate(row):
			if (c == 0 and int(col) < int(row[c+1]))\
			or (c == rl and int(col) < int(row[c-1]))\
			or (c > 0 and c < rl and int(col) < int(row[c-1]) and int(col) < int(row[c+1])):
				lowSpotIndexes.append([r, c])
	print("Number of low spots before filtering for y axis: " + str(len(lowSpotIndexes)))
	
	filteredLowSpotIndexes = []
	for i, item in enumerate(lowSpotIndexes):
		if checkVerticalsAreLarger(item):
			filteredLowSpotIndexes.append(item)
	return filteredLowSpotIndexes

def getLowSpotValues(indexes):
	return list(map(lambda x: int(heightmap[x[0]][x[1]]), indexes))

def getRiskValues(heights):
	return list(map(lambda h: 1 + h, heights))

def expand(point, checkedPoints):
	x = point[0]
	y = point[1]
	expanded = []
	checked = []
	targets = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
	for target in targets:
		if 0 <= target[0] < len(heightmap)\
		and 0 <= target[1] < len(heightmap[0])\
		and str(target) not in checkedPoints\
		and int(heightmap[target[0]][target[1]]) < 9:
			expanded.append(target)
		checked.append(str(target))
	return {
		"points": expanded,
		"checked": checked
	}

def getBasins(lowspots):
	basins = []
	for lowspot in lowspots:
		basin = [lowspot]
		targets = [lowspot]
		visited = []
		while len(targets) > 0:
			target = targets.pop()
			visited.append(str(target))
			expanded = expand(target, visited)
			targets =  targets + expanded["points"]
			basin += expanded["points"]
			visited += expanded["checked"]
		basins.append(basin)
	return basins



def part1():
	lowSpotIndexes = getLowSpots()
	print(lowSpotIndexes)
	lowSpotValues = getLowSpotValues(lowSpotIndexes)
	riskValues = getRiskValues(lowSpotValues)
	return sum(riskValues)

def part2():
	lowSpotIndexes = getLowSpots()
	basins = getBasins(lowSpotIndexes)
	basinSizes = sorted(list(map(lambda x: len(x), basins)), reverse=True)
	print(basinSizes)
	topThree = basinSizes[:3]
	return reduce(lambda x, y: x * y, topThree)


print("Part 1: " + str(part1()))
print("Part 2: " + str(part2()))
