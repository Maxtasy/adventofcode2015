# https://adventofcode.com/2015/day/21


WEAPONS = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]

ARMORS = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]

RINGS = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]

WARRIOR_HP = 100


def fight_boss(dmg, armor):
  warrior = WARRIOR_HP
  boss_hp = 109
  boss_dmg = 8
  boss_armor = 2

  warriors_turn = True

  while True:
    if warriors_turn:
      damage_dealt = max(dmg - boss_armor, 1)
      boss_hp -= damage_dealt

      if boss_hp <= 0:
        return True
    else:
      damage_dealt = max(boss_dmg - armor, 1)
      warrior -= damage_dealt

      if warrior <= 0:
        return False
      
    # change turns
    warriors_turn = not warriors_turn


def part2(input_file):
  maximum = 0

  # weapon, armor, two rings
  for weapon in WEAPONS:
    for armor in ARMORS:
      for i in range(len(RINGS) - 1):
        ring1 = RINGS[i]
        for j in range(i + 1, len(RINGS)):
          ring2 = RINGS[j]

          totals = []

          for i in range(3):
            totals.append(weapon[i] + armor[i] + ring1[i] + ring2[i])
          
          if totals[0] > maximum and not fight_boss(totals[1], totals[2]):
            maximum = totals[0]

  # weapon, armor, one ring
  for weapon in WEAPONS:
    for armor in ARMORS:
      for ring in RINGS:
        totals = []

        for i in range(3):
          totals.append(weapon[i] + armor[i] + ring[i])
        
        if totals[0] > maximum and not fight_boss(totals[1], totals[2]):
          maximum = totals[0]

  # weapon, armor
  for weapon in WEAPONS:
    for armor in ARMORS:
      totals = []

      for i in range(3):
        totals.append(weapon[i] + armor[i])
      
      if totals[0] > maximum and not fight_boss(totals[1], totals[2]):
        maximum = totals[0]

  # weapon
  for weapon in WEAPONS:
    if weapon[0] > maximum and not fight_boss(weapon[1], weapon[2]):
      maximum = weapon[0]

  # weapon, two rings
  for weapon in WEAPONS:
    for i in range(len(RINGS) - 1):
      ring1 = RINGS[i]
      for j in range(i + 1, len(RINGS)):
        ring2 = RINGS[j]

        totals = []

        for i in range(3):
          totals.append(weapon[i] + ring1[i] + ring2[i])
        
        if totals[0] > maximum and not fight_boss(totals[1], totals[2]):
          maximum = totals[0]

  # weapon, one ring
  for weapon in WEAPONS:
    for ring in RINGS:
      totals = []

      for i in range(3):
        totals.append(weapon[i] + ring[i])
      
      if totals[0] > maximum and not fight_boss(totals[1], totals[2]):
        maximum = totals[0]
  
  return maximum
      

def main():
	input_file = "day21-input.txt"
	print(part2(input_file))


if __name__ == "__main__":
	main()