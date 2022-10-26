import os

absolute_path = os.path.dirname(os.path.abspath(__file__))
filename = absolute_path + "/input.txt"
f = open(filename,"r")
instructions = f.readlines()

distance = 0
aim = 0
depth = 0

for i in instructions:
	parts = i.split(" ")
	command = parts[0]
	value = int(parts[1])
	if command == "up":
		aim -= value
	elif command == "down":
		aim += value
	else:
		distance += value
		depth += aim * value

print("Distance: " + str(distance))
print("Depth: " + str(depth))
print("Product: " + str(distance * depth))
