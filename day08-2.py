#https://adventofcode.com/2015/day/8


def part2(input_file):
	return sum(2 + stream.count("\\") + stream.count('"') for stream in open(input_file, "r"))


def main():
	input_file = "day08-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()