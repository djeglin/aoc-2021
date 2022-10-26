import os
import sys

args = sys.argv

absolute_path = os.path.dirname(os.path.abspath(__file__))
filename = absolute_path + "/input.txt"
f = open(filename,"r")
lines = f.readlines()
input = [{"signal": line.strip().split(' | ')[0].split(), "output": line.strip().split(' | ')[1].split()} for line in lines]

def p1(inp):
	o1478 = 0
	for i in inp:
		for o in i.get('output'):
			if len(o) in [2,3,4,7]:
				o1478 += 1
	return o1478

print("Number of occurrences of 1,4,7,8: " + str(p1(input)))

def getTopSegment(signal):
	s1 = ""
	s7 = ""
	for digit in signal:
		if len(digit) == 2:
			s1 = digit
		elif len(digit) == 3:
			s7 = digit
		if s1 != "" and s7 != "":
			break
	for key in s7:
		if key not in s1:
			return key

def getSegmentMap(line):
	signal = line.get("signal")
	segments = {
		"top": "",
		"middle": "",
		"bottom": "",
		"tl": "",
		"tr": "",
		"bl": "",
		"br": ""
	}

	segments["top"] = getTopSegment(signal)
	signalStr = " ".join(signal)

	counts = {
		"a": 0,
		"b": 0,
		"c": 0,
		"d": 0,
		"e": 0,
		"f": 0,
		"g": 0
	}
	
	for char in counts:
		counts[char] = signalStr.count(char)
	
	for char, count in counts.items():
		if count == 4:
			segments["bl"] = char
		elif count == 6:
			segments["tl"] = char
		elif count == 8:
			if char != segments["top"]:
				segments["tr"] = char
		elif count == 9:
			segments["br"] = char
		else: # count == 7
			s4 = ""
			for digit in signal:
				if len(digit) == 4:
					s4 = digit
					break
			if s4.count(char) > 0:
				segments["middle"] = char
			else:
				segments["bottom"] = char
	return segments

def decodeDigit(digit, segmentMap):
	digits = {
		2: ["top", "tr", "middle", "bl", "bottom"],
		3: ["top", "tr", "middle", "br", "bottom"],
		5: ["top", "tl", "middle", "br", "bottom"],
		0: ["top", "tl", "tr", "bl", "br", "bottom"],
		6: ["top", "tl", "middle", "bl", "br", "bottom"],
		9: ["top", "tl", "tr", "middle", "br", "bottom"],
	}
	digitArr = [*digit]
	for i in range(0, len(digitArr)):
		for key, value in segmentMap.items():
			if digitArr[i] == value:
				digitArr[i] = key
				break
	for key, value in digits.items():
		if all(x in digitArr for x in value) and all(y in value for y in digitArr):
			return key

def getDigits(line, segmentMap):
	digits = {
		0: "",
		1: "",
		2: "",
		3: "",
		4: "",
		5: "",
		6: "",
		7: "",
		8: "",
		9: ""
	}

	signal = line.get("signal")

	for digit in signal:
		if len(digit) == 2:
			digits[1] = digit
		elif len(digit) == 3:
			digits[7] = digit
		elif len(digit) == 4:
			digits[4] = digit
		elif len(digit) == 7:
			digits[8] = digit
		elif len(digit) == 5 or len(digit) == 6:
			key = decodeDigit(digit, segmentMap)
			digits[key] = digit
	
	return digits

def decodeOutput(line):
	signalMap = getSegmentMap(line)
	digits = getDigits(line, signalMap)
	output = ""
	for digit in line.get("output"):
		for key, value in digits.items():
			if all(x in digit for x in value) and all(y in value for y in digit):
				output += str(key)
				break
	return output

def p2(inp):
	values = []
	for i in range(len(inp)):
		values.append(int(decodeOutput(inp[i])))
	return sum(values)

print(p2(input))
