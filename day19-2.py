# https://adventofcode.com/2015/day/19


from random import shuffle


def part2(input_file):
  with open(input_file, "r") as f:
    replacement_str, molecule = f.read().strip().split("\n\n")

    replacements = []

    for line in replacement_str.split("\n"):
      line_parts = line.split(" => ")
      replacements.append([line_parts[0], line_parts[1]])
    
    target = molecule
    count = 0

    while target != "e":
      tmp = target
      for a, b in replacements:
        if b not in target:
          continue

        target = target.replace(b, a, 1)
        count += 1

      if tmp == target:
        target = molecule
        count = 0
        shuffle(replacements)

    return count
      

def main():
	input_file = "day19-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()