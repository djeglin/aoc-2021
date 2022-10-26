import os
import sys

args = sys.argv

absolute_path = os.path.dirname(os.path.abspath(__file__))
filename = absolute_path + "/input.txt"
f = open(filename,"r")
lines = f.readlines()

segments = [line.strip().split(' -> ') for line in lines]
# print(len(segments))

for segment in segments:
	segment[0] = list(map(int, segment[0].split(',')))
	segment[1] = list(map(int, segment[1].split(',')))

def getNonDiagonals():
	nonDiagonals = []
	for segment in segments:
		if segment[0][0] == segment[1][0] or segment[0][1] == segment[1][1]:
			nonDiagonals.append(segment)
	return nonDiagonals

def getDiagonals(nonDiagonals):
	return [segment for segment in segments if segment not in nonDiagonals]

def sortByX(e):
	return e[0]

def sortByY(e):
	return e[1]

def getLinePoints(set):
	lines = []
	for segment in set:
		if segment[0][0] == segment[1][0]:
			segment.sort(key=sortByY)
			for y in range(segment[0][1], segment[1][1] + 1):
				lines.append([segment[0][0], y])
		elif segment[0][1] == segment[1][1]:
			segment.sort(key=sortByX)
			for x in range(segment[0][0], segment[1][0] + 1):
				lines.append([x, segment[0][1]])
		else:
			segment.sort(key=sortByX)
			distance = segment[1][0] - segment[0][0]
			if segment[0][1] > segment[1][1]:
				for z in range(distance + 1):
					lines.append([segment[0][0] + z, segment[0][1] - z])
			else:
				for z in range(distance + 1):
					lines.append([segment[0][0] + z, segment[0][1] + z])

	return lines

def getIntersections(points):
	intersections = []
	for point in points:
		if point not in intersections:
			if points.count(point) > 1:
				intersections.append(point)
	return intersections


nonDiagonals = getNonDiagonals()
diagonals = getDiagonals(nonDiagonals)
# print(nonDiagonals)
points = getLinePoints(nonDiagonals + diagonals)
# print(points)
intersections = getIntersections(points)
# print(intersections)

print('Intersections: ' + str(len(intersections)))
