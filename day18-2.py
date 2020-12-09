# https://adventofcode.com/2015/day/18


from copy import deepcopy


STEPS = 100
GRID_ROWS = 100
GRID_COLS = 100


def number_of_lit_lights(arr, rows, cols):
    count = 0

    for row in range(rows):
      for col in range(cols):
        if arr[row][col]:
          count += 1
    
    return count


def part2(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

    light_states = []

    for row in range(GRID_ROWS):
      arr = []
      for col in range(GRID_COLS):
        if ((row == 0 and col == 0) or
            (row == 0 and col == GRID_COLS-1) or
            (row == GRID_ROWS-1 and col == 0) or
            (row == GRID_ROWS-1 and col == GRID_COLS-1)):
          arr.append(True)
        elif lines[row][col] == ".":
          arr.append(False)
        else:
          arr.append(True)
      light_states.append(arr)
    
    for _ in range(STEPS):
      light_states_copy = deepcopy(light_states)

      for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
          if ((row == 0 and col == 0) or
              (row == 0 and col == GRID_COLS-1) or
              (row == GRID_ROWS-1 and col == GRID_COLS-1) or
              (row == GRID_ROWS-1 and col == 0)):
            continue

          surrounding_lit_lights = 0

          for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):
              if row_offset == 0 and col_offset == 0:
                continue
              neighbor_row = row + row_offset
              neighbor_col = col + col_offset
              if neighbor_row >= 0 and neighbor_row < GRID_ROWS and neighbor_col >=0 and neighbor_col < GRID_COLS:
                if light_states_copy[neighbor_row][neighbor_col] == True:
                  surrounding_lit_lights += 1
          
          if light_states_copy[row][col] == True:
            if surrounding_lit_lights < 2 or surrounding_lit_lights > 3:
              light_states[row][col] = False
          else:
            if surrounding_lit_lights == 3:
              light_states[row][col] = True

    return number_of_lit_lights(light_states, GRID_ROWS, GRID_COLS)


def main():
	input_file = "day18-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()