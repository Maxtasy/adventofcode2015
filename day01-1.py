#https://adventofcode.com/2015/day/1


def part1(input_file):
	with open(input_file, "r") as f:
		sequence = f.read().strip()

	up = 0
	down = 0
	for c in sequence:
		if c == "(":
			up += 1
		elif c == ")":
			down += 1
		else:
			print("Invalid character in sequence.")
			return False
	floor = up - down

	return floor


def main():
	input_file = "day01-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()