#https://adventofcode.com/2015/day/11


import re


def part1(input_file):
	with open(input_file, "r") as f:
		password = f.read()

	while True:
		password = re.sub(r'([a-y])(z*)$', lambda x: chr(ord(x.group(1))+1) + len(x.group(2))*"a", password)

		if ("i" in password or "o" in password or "l" in password) or \
		   (len(re.findall(r'([a-z])\1', password)) < 2) or \
		   (len([1 for x, y, z in zip(password, password[1:], password[2:])
				   if ord(z)-ord(y) == 1 and ord(y)-ord(x) == 1]) == 0): continue

		return password


def main():
	input_file = "day11-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()