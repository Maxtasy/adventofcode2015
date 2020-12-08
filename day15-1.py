# https://adventofcode.com/2015/day/15


TEASPOONS = 100


def part1(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

    ingredients = {}

    for line in lines:
      name, properties_str = line.split(": ")
      ingredients[name] = {}
      properties_arr = properties_str.split(", ")
      for prop in properties_arr:
        prop_arr = prop.split(" ")
        prop_name = prop_arr[0]
        prop_value = int(prop_arr[1])
        ingredients[name][prop_name] = prop_value
    
    max_score = 0

    for i in range(1, TEASPOONS+1):
      for j in range(1, TEASPOONS+1 - i):
        for k in range(1, TEASPOONS+1 - i - j):
          for l in range(1, TEASPOONS+1 - i - j - k):
            capacity = i * ingredients["Sprinkles"]["capacity"] + j * ingredients["PeanutButter"]["capacity"] + k * ingredients["Frosting"]["capacity"] + l * ingredients["Sugar"]["capacity"]
            durability = i * ingredients["Sprinkles"]["durability"] + j * ingredients["PeanutButter"]["durability"] + k * ingredients["Frosting"]["durability"] + l * ingredients["Sugar"]["durability"]
            flavor = i * ingredients["Sprinkles"]["flavor"] + j * ingredients["PeanutButter"]["flavor"] + k * ingredients["Frosting"]["flavor"] + l * ingredients["Sugar"]["flavor"]
            texture = i * ingredients["Sprinkles"]["texture"] + j * ingredients["PeanutButter"]["texture"] + k * ingredients["Frosting"]["texture"] + l * ingredients["Sugar"]["texture"]
            
            capacity = max(capacity, 0)
            durability = max(durability, 0)
            flavor = max(flavor, 0)
            texture = max(texture, 0)

            score = capacity * durability * flavor * texture

            if score > max_score and i+j+k+l == TEASPOONS:
              max_score = score
              # print("New Score:", max_score, i, j, k, l)

    return max_score


def main():
	input_file = "day15-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()