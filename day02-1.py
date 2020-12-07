#https://adventofcode.com/2015/day/2


def part1(input_file):
	with open(input_file, "r") as f:
		lines = f.readlines()

	full_total = 0
	for line in lines:
		dimensions = line.split("x")
		dimensions = list(map(int, dimensions))
		a = dimensions[0] * dimensions[1]
		b = dimensions[1] * dimensions[2]
		c = dimensions[0] * dimensions[2]
		smallest_side = min(a, b, c)
		package_total = 2 * a + 2 * b + 2 * c + smallest_side
		full_total += package_total

	return full_total


def main():
	input_file = "day02-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()