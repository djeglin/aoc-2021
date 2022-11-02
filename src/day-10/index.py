import os
import sys
import math
from colorama import Fore, Style

args = sys.argv

absolute_path = os.path.dirname(os.path.abspath(__file__))
filename = absolute_path + "/input.txt"
f = open(filename,"r")
lines = f.readlines()

characterScores = {
	")": 3,
	"]": 57,
	"}": 1197,
	">": 25137
}

autocompleteScores = {
	")": 1,
	"]": 2,
	"}": 3,
	">": 4
}

pairs = {
	"(": ")",
	"[": "]",
	"{": "}",
	"<": ">"
}

def checkChar(chars, idx):
	length = len(chars)
	char = chars[idx]
	nIndex = idx + 1
	if chars[idx] in list(pairs.keys()):
		closing, closingIndex = checkChar(chars, nIndex)
		if closingIndex == 0:
			return ("", 0)
		if closing == pairs[char]:
			if closingIndex + 1 >= length:
				return ("", 0)
			else:
				next, nextIndex = checkChar(chars, closingIndex + 1)
				return (next, nextIndex)
		else:
			raise Exception(char, closing, pairs[char], closingIndex)
	else:
		return (char, idx)

scores = []
validLines = []

for i, line in enumerate(lines):
	chars = line.strip()
	try:
		char, idx = checkChar(chars, 0)
		print(Style.BRIGHT + str(i) + Style.RESET_ALL  + " OK")
		validLines.append(line)
	except Exception as e:
		if len(e.args) > 1:
			oChar, eChar, expected, eIdx = e.args
			print(
				Style.BRIGHT + str(i) + Style.RESET_ALL 
				+  " ERROR: Got " + Fore.RED + str(eChar) + Fore.RESET 
				+  " at index " + str(eIdx) 
				+ ", expected " + Fore.YELLOW + str(expected) + Fore.RESET 
				+ " for opening character " + Fore.YELLOW + str(oChar) + Fore.RESET
			)
			scores.append(characterScores.get(str(eChar)))

print("Sum of error scores for invalid lines: " + str(sum(scores)))
print("Number of valid lines: " + str(len(validLines)))

def autocomplete(chars):
	open = []
	openings = list(pairs.keys())
	for char in chars:
		if char in openings:
			open.append(char)
		else:
			if len(open) > 0:
				open.pop(-1)
	# print("Open characters: " + "".join(open))
	completion = ""
	if (len(open) > 0):
		for char in reversed(open):
			completion += pairs.get(char)
	# print("Completion: " + completion)
	return completion

completions = []
for i, line in enumerate(validLines):
	chars = line.strip()
	completion = autocomplete(chars)
	if len(completion) > 0:
		completions.append(completion)

def getAutocompletionScore(chars):
	score = 0
	for char in chars:
		score = score * 5 + autocompleteScores.get(char)
	return score

autocompleteScores = sorted([getAutocompletionScore(completion) for completion in completions])
print("Autocomplete scores: " + str(autocompleteScores))
print("Middle autocomplete score: " + str(autocompleteScores[math.floor(int(len(autocompleteScores) / 2))]))
