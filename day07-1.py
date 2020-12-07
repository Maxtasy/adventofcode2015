#https://adventofcode.com/2015/day/7


def part1(input_file):
	with open(input_file, "r") as f:
		lines = f.read().strip().split("\n")

	instructions = []

	for line in lines:
		instructions.append(line.split())

	values = {}

	while "a" not in values.keys():
		for instruction in instructions:
			if instruction[1] == "->":
				if instruction[0].isnumeric():
					if instruction[-1] not in values.keys():
						values[instruction[-1]] = int(instruction[0])
				elif instruction[0] in values.keys():
						values[instruction[-1]] = values[instruction[0]]
			elif instruction[0] == "NOT" and instruction[1] in values.keys():
				values[instruction[-1]] = int(~int(bin(values[instruction[1]]), 2))
			elif instruction[1] == "AND":
				if instruction[0].isnumeric() and instruction[2] in values.keys():
					values[instruction[-1]] = int(int(bin(int(instruction[0])), 2) & int(bin(values[instruction[2]]), 2))
				elif instruction[0] in values.keys() and instruction[2] in values.keys():
					values[instruction[-1]] = int(int(bin(values[instruction[0]]), 2) & int(bin(values[instruction[2]]), 2))
			elif instruction[1] == "OR":
				if instruction[0] in values.keys() and instruction[2] in values.keys():
					values[instruction[-1]] = int(int(bin(values[instruction[0]]), 2) | int(bin(values[instruction[2]]), 2))
			elif instruction[1] == "RSHIFT":
				if instruction[0] in values.keys():
					values[instruction[-1]] = int(int(bin(values[instruction[0]]), 2) >> int(instruction[2]))
			elif instruction[1] == "LSHIFT":
				if instruction[0] in values.keys():
					values[instruction[-1]] = int(int(bin(values[instruction[0]]), 2) << int(instruction[2]))

	return values["a"]


def main():
	input_file = "day07-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()