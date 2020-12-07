#https://adventofcode.com/2015/day/5


def part1(input_file):
	with open(input_file, "r") as f:
		lines = f.read().split("\n")

	def bad_check(line):
		bads = ["ab", "cd", "pq", "xy"]
		for bad in bads:
			if bad in line:
				return False
		return True

	def double_letter_check(line):
		for i in range(len(line) - 1):
			if line[i] == line[i+1]:
				return True
		return False

	def vowel_check(line):
		vowels = "aeiou"
		vowel_count = 0
		for c in line:
			if c in vowels:
				vowel_count += 1
		if vowel_count < 3:
			return False
		else:
			return True
		
	count = 0

	for line in lines:
		if bad_check(line) and double_letter_check(line) and vowel_check(line):
			count += 1

	return count


def main():
	input_file = "day05-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()