# https://adventofcode.com/2015/day/16


HINTS = {
  "children": 3,
  "cats": 7,
  "samoyeds": 2,
  "pomeranians": 3,
  "akitas": 0,
  "vizslas": 0,
  "goldfish": 5,
  "trees": 3,
  "cars": 2,
  "perfumes": 1
}


def part1(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

    aunts = {}

    for line in lines:
      line_parts = line.split(" ")
      aunt_id = int(line_parts[1][:-1])
      prop1 = line_parts[2][:-1]
      prop1_count = int(line_parts[3][:-1])
      prop2 = line_parts[4][:-1]
      prop2_count = int(line_parts[5][:-1])
      prop3 = line_parts[6][:-1]
      prop3_count = int(line_parts[7])

      aunts[aunt_id] = {}
      aunts[aunt_id][prop1] = prop1_count
      aunts[aunt_id][prop2] = prop2_count
      aunts[aunt_id][prop3] = prop3_count
    
    for aunt in aunts.keys():
      aunt_found = True
      for prop in aunts[aunt].keys():
        if aunts[aunt][prop] != HINTS[prop]:
          aunt_found = False
          break
      
      if aunt_found:
        return aunt


def main():
	input_file = "day16-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()