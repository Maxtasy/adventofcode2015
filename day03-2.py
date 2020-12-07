#https://adventofcode.com/2015/day/3


def part2(input_file):
	with open(input_file, "r") as f:
		stream = f.read().strip()

	visited_houses = []
	# x is horizontal
	# y is vertical
	# pos[x, y]
	santa_pos = [0, 0]
	bot_pos = [0, 0]

	for i in range(len(stream)):
		if i % 2 == 0:
			if stream[i] == "^":
				santa_pos[1] += 1
			elif stream[i] == "v":
				santa_pos[1] -= 1
			elif stream[i] == ">":
				santa_pos[0] += 1
			elif stream[i] == "<":
				santa_pos[0] -= 1
			else:
				print("Invalid move: " + stream[i])
			if str(santa_pos) not in visited_houses:
				visited_houses.append(str(santa_pos))
		elif i % 2 == 1:
			if stream[i] == "^":
				bot_pos[1] += 1
			elif stream[i] == "v":
				bot_pos[1] -= 1
			elif stream[i] == ">":
				bot_pos[0] += 1
			elif stream[i] == "<":
				bot_pos[0] -= 1
			else:
				print("Invalid move: " + stream[i])
			if str(bot_pos) not in visited_houses:
				visited_houses.append(str(bot_pos))

	return len(visited_houses)


def main():
	input_file = "day03-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()