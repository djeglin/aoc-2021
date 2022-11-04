import os
import sys
from colorama import Fore, Style

args = sys.argv

absolute_path = os.path.dirname(os.path.abspath(__file__))
filename = absolute_path + "/input.txt"
f = open(filename,"r")

cavePaths = list(i.strip() for i in f.readlines())
# Make sure that start and end paths are in the right arrangement,
# and add reverse paths for the rest so that we only have to check
# in one direction.
reversedPaths = []
for p,path in enumerate(cavePaths):
	if path.startswith("start") or path.endswith("end"):
		continue
	if path.endswith("start") or path.startswith("end"):
		parts = path.split("-")
		cavePaths[p] = parts[1] + "-" + parts[0]
		continue
	parts = path.split("-")
	reversedPaths.append(parts[1] + "-" + parts[0])
cavePaths = cavePaths + reversedPaths

# split paths into start and end points for ease of comparison
pathsArr = [i.split("-") for i in cavePaths]

def findRoutes(cave):
	# find all potential routes from a given cave
	global pathsArr
	routes = []
	for path in pathsArr:
		if path[0] == cave:
			routes.append(path)
	return routes

def findPaths(start, end, path=[]):
	# find all possible paths from start to end
	# path is a list of caves that we have already visited
	path = path + [start]
	paths = []
	if start == end:
		return [path]
	for cave in findRoutes(start):
		# we can only visit small caves once in a valid path
		# small caves are in lowercase letters
		if cave[1] not in path or not cave[1][0].islower():
			newpaths = findPaths(cave[1], end, path)
			for newpath in newpaths:
				paths.append(newpath)
	return paths

potentialPaths = findPaths("start", "end")
print("Potential paths: " + str(len(potentialPaths)))

# what would the paths look like if we could visit a single small cave
# exactly twice in a valid path?

def findPaths2(start, end, path=[], smallCaveRevisited=False):
	path = path + [start]
	paths = []
	if start == end:
		return [path]
	for cave in findRoutes(start):
		if cave[1] not in path or not cave[1][0].islower():
			newpaths = findPaths2(cave[1], end, path, smallCaveRevisited)
			for newpath in newpaths:
				paths.append(newpath)
		elif cave[1] in path and cave[1][0].islower() and not smallCaveRevisited:
			newpaths = findPaths2(cave[1], end, path, True)
			for newpath in newpaths:
				paths.append(newpath)
	return paths

potentialPaths2 = findPaths2("start", "end")
print("Potential paths with small cave revisited: " + str(len(potentialPaths2)))
