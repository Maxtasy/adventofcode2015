#https://adventofcode.com/2015/day/8


def part1(input_file):
	with open(input_file, "r") as f:
		stream = f.read().strip().split("\n")

	code_size = 0
	memory_size = 0

	for part in stream:
		code_size += len(part)
		memory_size += len(eval(part))

	return code_size - memory_size


def main():
	input_file = "day08-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()