import os
import sys
from colorama import Fore, Style

args = sys.argv

absolute_path = os.path.dirname(os.path.abspath(__file__))
filename = absolute_path + "/input.txt"
f = open(filename,"r")
lines = f.readlines()

template = lines.pop(0).strip()

lines = list(filter(lambda x: x.strip() != "", lines))
rules = dict(r.strip().split(" -> ") for r in lines)

def getInitialPairs():
	global template
	global rules
	pairs = {r:0 for r in rules.keys()}
	for i in range(len(template) - 1):
		pair = template[i:i+2]
		pairs[pair] += 1
	return pairs


def doStep(pairs):
	global rules
	newPairs = {p:0 for p in pairs}
	for pair in pairs:
		lPair = pair[0] + rules.get(pair)
		rPair = rules.get(pair) + pair[1]
		newPairs[lPair] += pairs[pair]
		newPairs[rPair] += pairs[pair]
	return newPairs

def getCharCounts(pairs):
	global template
	chars = {}
	for pair in pairs:
		char = pair[0]
		chars[char] = chars.get(char, 0) + pairs[pair]
	chars[template[-1]] += 1 # because we never count the last character of the template
	return chars
	
def main():
	global template
	pairs = getInitialPairs()
	for i in range(40):
		pairs = doStep(pairs)
	counts = getCharCounts(pairs)
	print("Most common character: " + max(counts, key=counts.get))
	print("Least common character: " + min(counts, key=counts.get))
	print("Most - Least: " + str(counts[max(counts, key=counts.get)] - counts[min(counts, key=counts.get)]))

main()

