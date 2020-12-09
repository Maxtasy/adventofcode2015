# https://adventofcode.com/2015/day/17


from itertools import combinations


LITERS = 150


def part2(input_file):
  with open(input_file, "r") as f:
    containers = list(map(int, f.read().strip().split("\n")))
    
    least_containers = len(containers)
    total_combinations = 0

    for i in range(1, len(containers) + 1):
      combs = list(combinations(containers, i))
      for comb in combs:
        if sum(comb) == LITERS:
          if len(comb) < least_containers:
            least_containers = len(comb)
            total_combinations = 1
          elif len(comb) == least_containers:
            total_combinations += 1
    
    return total_combinations


def main():
	input_file = "day17-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()