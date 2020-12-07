# https://adventofcode.com/2015/day/12


import json


def part2(input_file):

	def unwrap(data_object):
		if type(data_object) == int:
			return data_object
		if type(data_object) == list:
			return sum([unwrap(sub_object) for sub_object in data_object])
		if type(data_object) != dict:
			return 0
		if "red" in data_object.values():
			return 0
		return unwrap(list(data_object.values()))

	with open(input_file, "r") as f:
		data = json.load(f)

	return unwrap(data)
		


def main():
	input_file = "day12-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()