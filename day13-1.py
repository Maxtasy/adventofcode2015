# https://adventofcode.com/2015/day/13


from itertools import permutations


def part1(input_file):
  with open(input_file, "r") as f:
    input_arr = f.read().strip().split("\n")

    guests = {}
    scores = []

    for line in input_arr:
      line_parts = line.replace(".", "").split(" ")
      self_name = line_parts[0]

      if not guests.get(self_name):
        guests[self_name] = {}

      contact_name = line_parts[-1]
      happiness_score = int(line_parts[3])
      if line_parts[2] == "lose":
        happiness_score *= -1

      guests[self_name][contact_name] = happiness_score
    
    perms = list(permutations(guests.keys()))
    
    for perm in perms:
      perm = list(perm)
      perm_score = 0
      for i in range(len(perm)):
        person_score = guests[perm[i]][perm[i-1]] + guests[perm[i]][perm[(i+1) % len(perm)]]
        perm_score += person_score
      
      scores.append(perm_score)
  
    return max(scores)


def main():
	input_file = "day13-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()