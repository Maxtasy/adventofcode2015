#https://adventofcode.com/2015/day/10


from itertools import groupby


def part2(input_file, iterations=50):
	with open(input_file, "r") as f:
		puzzle_input = f.read()

	for _ in range(iterations):
		puzzle_input = ''.join(str(len(list(v))) + k for k, v in groupby(puzzle_input))

	return len(puzzle_input)


def main():
	input_file = "day10-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()