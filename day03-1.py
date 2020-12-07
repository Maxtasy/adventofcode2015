#https://adventofcode.com/2015/day/3


def part1(input_file):
	with open(input_file, "r") as f:
		stream = f.read().strip()

	visited_houses = []
	# x is horizontal
	# y is vertical
	# pos[x, y]
	pos = [0, 0]

	for c in stream:
		
		if c == "^":
			pos[1] += 1
		elif c == "v":
			pos[1] -= 1
		elif c == ">":
			pos[0] += 1
		elif c == "<":
			pos[0] -= 1
		else:
			print("Invalid move: " + c)

		if str(pos) not in visited_houses:
			visited_houses.append(str(pos))

	return len(visited_houses)


def main():
	input_file = "day03-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()