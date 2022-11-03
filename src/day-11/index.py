import os
import sys
import math
from colorama import Fore, Style

args = sys.argv

absolute_path = os.path.dirname(os.path.abspath(__file__))
filename = absolute_path + "/input.txt"
f = open(filename,"r")
lines = f.readlines()
matrix = [list( map(int,i.strip()) ) for i in lines.copy()]

def toZero(n):
	return 0

def increment(n):
	return n + 1

print(Style.BRIGHT + "Initial octopus map:" + Style.RESET_ALL)
for i in matrix:
	print(" ".join( map(str,i) ))


def getAdjacent(y, x):
	ly = len(matrix)
	lx = len(matrix[0])
	adjascent = []
	for i in range(y - 1, y + 2):
		for j in range(x - 1, x + 2):
			if i == y and j == x:
				continue
			if i < 0 or j < 0 or i >= ly or j >= lx:
				continue
			adjascent.append([i, j])
	return adjascent

def increaseEnergy(coords, matrix, lights):
	m = matrix.copy()
	l = lights.copy()
	lightsCount = 0
	toIncrease = []
	for c in coords:
		m[c[0]][c[1]] += 1
	for y, row in enumerate(m):
		for x, cell in enumerate(row):
			if cell > 9 and l[y][x] == 0:
				l[y][x] = 1
				lightsCount += 1
				adjascent = getAdjacent(y, x)
				for i in adjascent:
					if str(i) not in [map(str, toIncrease)]:
						toIncrease.append(i)
	return m, lights, lightsCount, toIncrease

def resetFlashes(matrix):
	for y, row in enumerate(matrix):
		for x, cell in enumerate(row):
			if cell > 9:
				matrix[y][x] = 0
	return matrix


def step(matrix):
	localMatrix = matrix.copy()
	toIncrease = []
	for y, row in enumerate(localMatrix):
		for x, cell in enumerate(row):
			toIncrease.append([y, x])
	lights = [list( map(toZero,i.strip()) ) for i in lines.copy()]
	totalLights = 0
	lightsCount = math.inf
	i = 1
	while lightsCount > 0:
		localMatrix, lights, lightsCount, toIncrease = increaseEnergy(toIncrease, localMatrix, lights)
		# print("Flashes in iteration " + str(i) + ": " + str(lightsCount))
		totalLights += lightsCount
		i += 1
	localMatrix = resetFlashes(localMatrix)
	return localMatrix, totalLights

def p1():
	m = matrix.copy()
	totalLights = 0
	allFlashStep = -1
	i = 0
	while allFlashStep < 0:
		m, stepLights = step(m)
		totalLights += stepLights
		print("Flashes in step " + str(i + 1) + ": " + str(stepLights))
		if stepLights == 100:
			allFlashStep = i + 1
		i += 1
	print("First step where all octopuses flash: " + str(allFlashStep))
	return totalLights

print("Total flashes: " + str(p1()))
