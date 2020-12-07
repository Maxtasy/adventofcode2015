#https://adventofcode.com/2015/day/2


def part2(input_file):
	with open(input_file, "r") as f:
		lines = f.readlines()

	full_total = 0
	for line in lines:
		dimensions = line.split("x")
		dimensions = list(map(int, dimensions))
		dimensions.sort()
		ribbon = 2 * dimensions[0] + 2 * dimensions[1]
		bow = dimensions[0] * dimensions[1] * dimensions[2]
		package_total = ribbon + bow
		full_total += package_total
	
	return full_total


def main():
	input_file = "day02-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()