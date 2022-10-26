import os

absolute_path = os.path.dirname(os.path.abspath(__file__))
filename = absolute_path + "/input.txt"
f = open(filename,"r")
lines = f.readlines()

gamma = []

dataLength = len(lines)

for i, val in enumerate(lines[0].strip()):
	ones = 0
	zeros = 0
	for j in lines:
		if ones > dataLength / 2 or zeros > dataLength / 2:
			break
		if j[i] == "1":
			ones += 1
		else:
			zeros += 1
	if ones > zeros:
		gamma.append(1)
	else:
		gamma.append(0)

def flipBit(bit):
	if bit == 0:
		return 1
	else:
		return 0

epsilon = map(flipBit, gamma)

gammaStr = ''.join(map(str, gamma))
epsilonStr = ''.join(map(str, epsilon))

print("Gamma: ", gammaStr)
print("Epsilon: ", epsilonStr)

power = int(gammaStr, 2) * int(epsilonStr, 2)

def getMostLeastPopularBit(digit, array, mode):
	ones = 0
	zeros = 0
	for i in array:
		if ones > len(array) / 2 or zeros > len(array) / 2:
			break
		if i[digit] == "1":
			ones += 1
		else:
			zeros += 1
	if mode == "most":
		if ones >= zeros:
			return 1
		else:
			return 0
	if mode == "least":
		if zeros <= ones:
			return 0
		else:
			return 1

def getRating(type):
	if type == "oxygen":
		mode = "most"
	else:
		mode = "least"
	values = lines
	digit = 0
	while len(values) > 1:
		bit = getMostLeastPopularBit(digit, values, mode)
		newValues = [i for i in values if int(i[digit]) == bit]
		values = newValues
		digit += 1
	return values[0].strip()



print("Power: ", int(gammaStr, 2), " x ", int(epsilonStr, 2), " = ", power)

print("Oxy Rating: ", getRating("oxygen"))
print("CO2 Rating: ", getRating("co2"))

print("Life support rating: ", int(getRating("oxygen"), 2) * int(getRating("co2"), 2))
