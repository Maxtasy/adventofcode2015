#https://adventofcode.com/2015/day/5


def part2(input_file):
	with open("day05-input.txt", "r") as f:
		lines = f.read().split("\n")

	def repeat_check(line):
		for i in range(len(line) - 2):
			if line[i] == line[i + 2]:
				return True
		return False

	def pair_check(line):
		for i in range(len(line) - 1):
			pair = line[i] + line[i + 1]
			if pair in line[i + 2:]:
				return True
		return False

	count = 0

	for line in lines:
		if repeat_check(line) and pair_check(line):
			count += 1

	return count


def main():
	input_file = "day05-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()