import os
import sys

args = sys.argv

absolute_path = os.path.dirname(os.path.abspath(__file__))
filename = absolute_path + "/input.txt"
f = open(filename,"r")
crabs = list(map(int, f.readline().split(',')))

crabs.sort()
mid = len(crabs) // 2
median = (crabs[mid] + crabs[~mid]) // 2

def get_arithmetic_sum(steps):
    return int((((2) + (steps - 1)) / 2) * steps)

p1Fuel = sum([abs(median - i) for i in crabs])

def p2Fuel(data):
	fuel_burn = lambda x, p: abs(x-p)*(abs(x-p) + 1)//2
	return min([sum(fuel_burn(x, i) for x in data) for i in range(max(data))])

print(crabs)
print('Number of crabs:', len(crabs))
print('Median crab:', crabs[median])
print('Fuel for part 1:', p1Fuel)
print('Fuel for part 2:', p2Fuel(crabs))
