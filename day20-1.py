# https://adventofcode.com/2015/day/20


from collections import defaultdict


UPPER_BOUND = 1000000


def part1(input_file):
  with open(input_file, "r") as f:
    target = int(f.read().strip())
    
    houses = defaultdict(int)

    for elf in range(1, target):
      for house in range(elf, UPPER_BOUND, elf):
        houses[house] += elf * 10
      
      if houses[elf] >= target:
        return elf
      

def main():
	input_file = "day20-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()