#https://adventofcode.com/2015/day/1


def part2(input_file):
	with open(input_file, "r") as f:
		sequence = f.read().strip()
		
	pos = 0
	for i in range(len(sequence)):
		if sequence[i] == "(":
			pos += 1
		elif sequence[i] == ")":
			pos -= 1
		else:
			print("Invalid character in sequence.")
			return None
		if pos == -1:
			return i + 1
	return None


def main():
	input_file = "day01-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()