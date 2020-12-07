#https://adventofcode.com/2015/day/9


import sys
from itertools import permutations


def part1(input_file):
	# Set up out data structure
	with open(input_file, "r") as f:
		places = set()
		distances = dict()

		for line in f.readlines():
			source, _, dest, _, distance = line.split()
			places.add(source)
			places.add(dest)

			distances.setdefault(source, dict())[dest] = int(distance)
			distances.setdefault(dest, dict())[source] = int(distance)
			
	shortest = sys.maxsize
	longest = 0
	for items in permutations(places):
		dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
		shortest = min(shortest, dist)
		longest = max(longest, dist)

	return shortest, longest
	

def main():
	input_file = "day09-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()