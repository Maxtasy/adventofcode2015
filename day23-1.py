# https://adventofcode.com/2015/day/21


def part1(input_file):
  with open(input_file, "r") as f:
    instructions = f.read().strip().replace(",", "").split("\n")

    registers = {
      "a": 0,
      "b": 0
    }

    cur_index = 0

    while cur_index >= 0 and cur_index < len(instructions):
      instr = instructions[cur_index].split()
      if instr[0] == "hlf":
        register = instr[1]
        registers[register] //= 2
        cur_index += 1
      elif instr[0] == "tpl":
        register = instr[1]
        registers[register] *= 3
        cur_index += 1
      elif instr[0] == "inc":
        register = instr[1]
        registers[register] += 1
        cur_index += 1
      elif instr[0] == "jmp":
        prefix = instr[1][0]
        offset = int(instr[1][1:])
        if prefix == "-":
          offset *= -1
        cur_index += offset
      elif instr[0] == "jie":
        register = instr[1]
        if registers[register] % 2 == 0:
          prefix = instr[2][0]
          offset = int(instr[2][1:])
          if prefix == "-":
            offset *= -1
          cur_index += offset
        else:
          cur_index += 1
      elif instr[0] == "jio":
        register = instr[1]
        if registers[register] == 1:
          prefix = instr[2][0]
          offset = int(instr[2][1:])
          if prefix == "-":
            offset *= -1
          cur_index += offset
        else:
          cur_index += 1
      else:
        print("Unexpected instruction", instr)
        break
    
    return registers["b"]
      

def main():
	input_file = "day23-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()