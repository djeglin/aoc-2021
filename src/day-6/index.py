import os
import sys

args = sys.argv

absolute_path = os.path.dirname(os.path.abspath(__file__))
filename = absolute_path + "/input.txt"
f = open(filename,"r")
school = list(map(int, f.readline().split(',')))

groups = [0,0,0,0,0,0,0,0,0]
for fish in school:
	groups[fish] += 1

days = 256

def updateGroups(g):
	i = 8
	new = [0,0,0,0,0,0,0,0,0]
	while i >= 0:
		if i == 0:
			new[8] += g[0]
			new[6] += g[0]
		else:
			new[i - 1] += g[i]
		i -= 1
	return new

while days > 0:
	groups = updateGroups(groups)
	days -= 1

print(sum(groups))
