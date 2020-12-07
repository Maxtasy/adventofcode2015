#https://adventofcode.com/2015/day/10


def apply_look_and_say(num_in):
	num_out = str()

	while num_in:
		elem = num_in[0]
		count = 1

		for i in range(1, len(num_in)):
			if num_in[i] == elem:
				count += 1
			else:
				break

		num_out += str(count) + elem
		num_in = num_in[count:]

	return num_out


def part1(input_file):
	with open(input_file, "r") as f:
		puzzle_input = f.read()

	for i in range(40):
		puzzle_input = apply_look_and_say(puzzle_input)

	return len(puzzle_input)


def main():
	input_file = "day10-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()