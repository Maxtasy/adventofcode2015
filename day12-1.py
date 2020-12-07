#https://adventofcode.com/2015/day/12


def part1(input_file):
	with open(input_file, "r") as f:
		s = f.read()

		mask = "-0123456789"
		cleaned = ""

		for l in s:
			if l in mask:
				cleaned += l
			else:
				cleaned += " "

		return sum(map(int, cleaned.split()))


def main():
	input_file = "day12-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()