# https://adventofcode.com/2015/day/24


from collections import defaultdict


TARGET_ROW = 3010
TARGET_COL = 3019

def part1():
  grid = defaultdict(int)

  code = 20151125
  pos = [0, 0]
  
  grid_size = 0

  while grid[(TARGET_ROW, TARGET_COL)] == 0:
    if pos[0] < 1:
      grid_size += 1
      pos[0] = grid_size
      pos[1] = 1
      # print("Added new row/col")
    
    grid[(pos[0], pos[1])] = code
    
    pos[0] -= 1
    pos[1] += 1

    code = (code * 252533) % 33554393
  
  return grid[(TARGET_ROW, TARGET_COL)]
      

def main():
	print(part1())


if __name__ == "__main__":
	main()