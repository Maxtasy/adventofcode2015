# https://adventofcode.com/2015/day/22
# thx to https://www.reddit.com/r/adventofcode/comments/3xspyl/day_22_solutions/cy7mbfz/?utm_source=share&utm_medium=web2x&context=3


from copy import deepcopy
from sys import maxsize


BOSS_HP = 58
BOSS_DMG = 9

# 0=manacost, 1=dmg, 2=hp, 3=armour, 4=mana, 5=turns, 6=index
missile = (53,4,0,0,0,0,0)
drain = (73,2,2,0,0,0,1)
shield = (113,0,0,7,0,6,2)
poison = (173,3,0,0,0,6,3)
recharge = (229,0,0,0,101,5,4)
spells = [missile, drain, shield, poison, recharge]
leastManaUsed = maxsize
partTwo = True


def sim(bossHP, myHP, myMana, activespells, playerTurn, manaUsed):
    bossDmg = BOSS_DMG
    myArmour = 0

    if partTwo and playerTurn:
        myHP -= 1
        if myHP <= 0:
            return False
            
    newActiveSpells = []
    for activespell in activespells:
        if activespell[5] >= 0: # spell effect applies now
            bossHP -= activespell[1]
            myHP += activespell[2]
            myArmour += activespell[3]
            myMana += activespell[4]

        newActiveSpell = (activespell[0], activespell[1], activespell[2], activespell[3], activespell[4], activespell[5]-1, activespell[6])
        if newActiveSpell[5] > 0: # spell carries over
            newActiveSpells.append(newActiveSpell)
    
    if bossHP <= 0:
        global leastManaUsed
        if manaUsed < leastManaUsed:
            leastManaUsed = manaUsed
        return True

    if manaUsed >= leastManaUsed:
        return False

    if (playerTurn):
        for i in range(len(spells)):
            spell = spells[i]
            spellAlreadyActive = False
            for j in range(len(newActiveSpells)):
                if newActiveSpells[j][6] == spell[6]:
                    spellAlreadyActive = True
                    break

            spellManaCost = spell[0]
            if spellManaCost <= myMana and not spellAlreadyActive:
                a = deepcopy(newActiveSpells)
                a.append(spell)
                sim(bossHP, myHP, myMana - spellManaCost, a, False, manaUsed+spellManaCost)
    else:
        myHP += myArmour-bossDmg if myArmour-bossDmg < 0 else -1
        if myHP > 0:
            sim(bossHP,myHP,myMana,newActiveSpells, True,manaUsed)


def part1(input_file):
  sim(BOSS_HP,50,500,[],True,0)

  return leastManaUsed


def main():
	input_file = "day21-input.txt"
	print(part1(input_file))


if __name__ == "__main__":
	main()