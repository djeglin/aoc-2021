import os

from functools import reduce
from operator import add

absolute_path = os.path.dirname(os.path.abspath(__file__))
filename = absolute_path + "/input.txt"
f = open(filename,"r")

depths = [int(numeric_string) for numeric_string in f.readlines()]

d = 0
prev = None

windows = []

for i, value in enumerate(depths):
	if i + 2 < len(depths):
		windows.append(reduce(add, depths[i:i+3]))


for depth in windows:
	if prev is not None and prev < depth:
		d += 1
	prev = depth

print(d)
