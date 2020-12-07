# https://adventofcode.com/2015/day/14


RACE_DURATION = 2503


def part2(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

    reindeers = {}

    for line in lines:
      line_parts = line.split(" ")
      name = line_parts[0]

      reindeers[name] = {}

      reindeers[name]["speed"] = int(line_parts[3])
      reindeers[name]["flying_duration"] = int(line_parts[6])
      reindeers[name]["resting_duration"] = int(line_parts[-2])
      reindeers[name]["flying"] = True
      reindeers[name]["timer"] = reindeers[name]["flying_duration"]
      reindeers[name]["distance"] = 0
      reindeers[name]["points"] = 0

    furthest_distance = 0
    most_points = 0

    for _ in range(RACE_DURATION):
      furthest_reindeer = []

      for key in reindeers.keys():
        reindeer = reindeers[key]
        if reindeer["flying"]:
          reindeer["distance"] += reindeer["speed"]

        reindeer["timer"] -= 1

        if reindeer["timer"] <= 0:
          reindeer["flying"] = not reindeer["flying"]

          if reindeer["flying"]:
            reindeer["timer"] = reindeer["flying_duration"]
          else:
            reindeer["timer"] = reindeer["resting_duration"]
        
        if reindeer["distance"] > furthest_distance:
          furthest_distance = reindeer["distance"]
          furthest_reindeer = [key]
        elif reindeer["distance"] == furthest_distance:
          furthest_reindeer.append(key)
      
      for name in furthest_reindeer:
        reindeers[name]["points"] += 1
        most_points = max(reindeers[name]["points"], most_points)

    return most_points


def main():
	input_file = "day14-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()