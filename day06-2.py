#https://adventofcode.com/2015/day/6


def part2(input_file):
	with open(input_file, "r") as f:
		lines = f.read().strip().split("\n")

	grid = {}

	for i in range(1000):
		for j in range(1000):
			grid[(j, i)] = 0
	 
	instructions = []

	for line in lines:
		instruction = []
		offset = 0
		parts = line.split()
		action = parts[0]
		if parts[0] == "turn":
			offset = 1
			action += " " + parts[1]
		start = parts[1 + offset].split(",")
		end = parts[3 + offset].split(",")
		first = (int(start[0]), int(start[1]))
		last = (int(end[0]), int(end[1]))
		instruction.append(action)
		instruction.append(first)
		instruction.append(last)
		instructions.append(instruction)

	for instruction in instructions:
		if instruction[0] == "turn on":
			for i in range(instruction[1][0], instruction[2][0] + 1):
				for j in range(instruction[1][1], instruction[2][1] + 1):
					grid[(i, j)] += 1
		elif instruction[0] == "turn off":
			for i in range(instruction[1][0], instruction[2][0] + 1):
				for j in range(instruction[1][1], instruction[2][1] + 1):
					if grid[(i, j)] > 0:
						grid[(i, j)] -= 1
		elif instruction[0] == "toggle":
			for i in range(instruction[1][0], instruction[2][0] + 1):
				for j in range(instruction[1][1], instruction[2][1] + 1):
					grid[(i, j)] += 2

	count = 0

	for value in grid.values():
		count += value
		
	return count


def main():
	input_file = "day06-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()