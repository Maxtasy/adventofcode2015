#https://adventofcode.com/2015/day/4


import hashlib


def part2(input_file):
	with open(input_file, "r") as f:
		prefix = f.read()

	num = 0

	while not found:
		key = prefix + str(num)
		hashed = hashlib.md5(key.encode('utf-8')).hexdigest()
		if hashed[:6] == "000000":
			return num
		else:
			num += 1


def main():
	input_file = "day04-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()