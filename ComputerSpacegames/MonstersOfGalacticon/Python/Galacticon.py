import random
import os
import time


def main():
    print("MONSTERS OF GALACTICON")
    monster_names = [""] * 6
    monster_count = 4
    member_count = 5
    monster_names[1] = "SULFACIDOR"
    monster_names[2] = "FLAMGONDAR"
    monster_names[3] = "BALNOLOTIN"
    monster_names[4] = "GOLANDOR"
    shuffle(monster_names , monster_count)

    for times in range(1, 9):
        os.system("cls")
        random_monster = random.randint(1, monster_count)
        print("MONSTER COMING...")
        print("IT'S A ", monster_names[random_monster])
        print("WHICH WEAPON ? (R, S OR T)  ")
        weapon_choice = input()
        accuracy = abs(ord(weapon_choice) - 81 - random_monster)
        if accuracy == 0:
            killed_one()
            time.sleep(2) # Sleep 2 seconds
            continue

        if accuracy != 1:
            print("NO USE. IT'S EATEN ONE")
            print("OF YOUR GROUP")
            member_count = lose_one(member_count)
            time.sleep(2) # Sleep 2 seconds
            continue

        print("NO EFFECT")
        if random.random() <= 0.4:
            print("YOU ANGERED THE ", monster_names[random_monster], " AND IT")
            print("KILLED ONE OF YOUR GROUP")
            member_count = lose_one(member_count)
            time.sleep(2) # Sleep 2 seconds
            continue
                
        time.sleep(2) # Sleep 2 seconds

    print("YOU SURVIVED TO")
    print("CONQUER GALACTICON")
    exit(1)

def shuffle(monster_names, monster_count):
    for I in range(1, (monster_count)+1):
        option1 = random.randint(1, monster_count)
        option2 = random.randint(1, monster_count)
        monster_names[option1],monster_names[option2] = monster_names[option2],monster_names[option1]

def killed_one():
	print("YOU'VE KILLED IT")
	return

def lose_one(member_count = None):
	member_count = member_count - 1
	if member_count < 1:
		dead()

	return member_count

def dead():
	print("YOU'RE ALL DEAD")
	exit(1)


main()
