import os
import random
import msvcrt
import time

def main():
    difficulty = introduction()
    shotdown = 0
    for go in range(1, 11):
        shotdown = one_game(shotdown, difficulty)
        
    print("YOU HIT ", shotdown, "/10")


def introduction():
    os.system("cls")
    print("ALIEN SNIPERS")
    print()
    print("DIFFICULTY (1-10)")

    while True:
        difficulty = int(input())
        if not (difficulty < 1 or difficulty > 10):
            break

    return difficulty


def one_game(shotdown, difficulty):
    letter = chr(random.randint(65, 65 + (26 - difficulty)))
    numberafterletter = random.randint(1, 1 + difficulty)
    
    os.system("cls")
    print(letter, "	", numberafterletter)

    for I in range(1, 100000 + difficulty * 5000):
        key_pressed = get_input()
        if key_pressed != "":
            shotdown = validate_shot(shotdown, key_pressed, letter, numberafterletter)
            return shotdown

    print("too slow")
    time.sleep(2)
    return shotdown
    

def get_input():
    if msvcrt.kbhit():
        ch = msvcrt.getch()
        result = ch.decode('ascii')
        return result
    return ''


def validate_shot(shotdown,  key_pressed,  letter,  numberafterletter):
    target_letter = chr(ord(letter) + numberafterletter)
    if key_pressed == target_letter:
        print("good shot")
        shotdown = shotdown + 1
    else:
        print("missed")

    time.sleep(2)
    return shotdown


main()