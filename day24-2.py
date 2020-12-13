# https://adventofcode.com/2015/day/24


import itertools
import operator
import functools


PARTS = 4


def hasSum(lst, tot, sub):
  for y in range(1,len(lst)): 
    for x in (z for z in itertools.combinations(lst, y) if sum(z) == tot):
      if sub == 2:
        return True
      elif sub < PARTS:
        return hasSum(list(set(lst) - set(x)), tot, sub - 1)
      elif hasSum(list(set(lst) - set(x)), tot, sub - 1):
        return functools.reduce(operator.mul, x, 1)


def part2(input_file):
  with open(input_file, "r") as f:
    packages = list(map(int, f.read().strip().split("\n")))
    
    group_weight = sum(packages) // PARTS
    
    return hasSum(packages, group_weight, PARTS)
      

def main():
	input_file = "day24-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()