# https://adventofcode.com/2015/day/19


def part1(input_file):
  with open(input_file, "r") as f:
    replacement_str, molecule = f.read().strip().split("\n\n")

    replacements = []
    modified = []

    for line in replacement_str.split("\n"):
      line_parts = line.split(" => ")
      replacements.append([line_parts[0], line_parts[1]])
    
    for i in range(len(replacements)):
      search_str = replacements[i][0]
      search_str_len = len(search_str)
      replace_str = replacements[i][1]

      for index in range(len(molecule)):
        if molecule[index:index + search_str_len] == search_str:
          pre = molecule[:index]
          post = molecule[index + search_str_len:]
          modified_molecule = pre + replace_str + post

          if modified_molecule not in modified:
            modified.append(modified_molecule)

    return len(modified)
      

def main():
	input_file = "day19-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()