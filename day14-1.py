# https://adventofcode.com/2015/day/14


RACE_DURATION = 2503


def part1(input_file):
  with open(input_file, "r") as f:
    lines = f.read().strip().split("\n")

    reindeers = []
    distances = []

    for line in lines:
      line_parts = line.split(" ")
      
      reindeer = {}
      
      reindeer["speed"] = int(line_parts[3])
      reindeer["fly_duration"] = int(line_parts[6])
      reindeer["resting_duration"] = int(line_parts[-2])

      reindeers.append(reindeer)
    
    for reindeer in reindeers:
      state = 1 #1 - flying, 0 - resting
      distance = 0
      fly_timer = 0
      rest_timer = 0

      for _ in range(RACE_DURATION):
        if state == 1:
          distance += reindeer["speed"]
          fly_timer += 1
          if fly_timer >= reindeer["fly_duration"]:
            state = 0
            fly_timer = 0
        elif state == 0:
          rest_timer += 1
          if rest_timer >= reindeer["resting_duration"]:
            state = 1
            rest_timer = 0

      distances.append(distance)
    
    return max(distances)


def main():
	input_file = "day14-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()