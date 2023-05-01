import os
import time
import random
import sys

import msvcrt

def get_input():
    if msvcrt.kbhit():
        ch = msvcrt.getch()
        result = str(ch.decode('ascii'))
        return result

    return ''

def function_350(D = None,  A = None):
    sys.stdout.write("\033["+str(D)+";"+str(A)+"H")
    return

def position1():
    D = 10
    A = 1
    function_350(D, A)
    return

def position2():
    D = 1
    A = 20
    function_350(D, A)
    return

def position3():
    D = 10
    A = 40
    function_350(D, A)
    return

def position4():
    D = 20
    A = 20
    function_350(D, A)
    return

def set_position(R):
    if R == 1:
        position1()

    if R == 2:
        position2()

    if R == 3:
        position3()

    if R == 4:
        position4()

def blink(R):
    set_position(R)
    print("OO")

def pop(R):
    set_position(R)
    print("*")

def main():
    os.system("cls")
    print("BUG EYES")
    S = 0
    position1()
    print('1')

    position2()
    print('2')

    position3()
    print('3')

    position4()
    print('4')
    time.sleep(5)

    for T in range(1, 11):
        os.system("cls")
        if T > 1:
            print(f"{S}/{T-1}")

        waits = (random.randint(2000, 7000)) / 1000
        time.sleep(waits) # Sleep (random.randint(2000, 3000)) / 1000 seconds
        R = random.randint(1, 4)

        blink(R)
        for I in range(1, 80000+1):
            R_string = get_input()
            if R_string != "":
                break

        if (int(R_string) if len(R_string)>0 else 0) != R:
            continue

        S = S + 1
        os.system("cls")

        pop(R)

        time.sleep(3) # Sleep 3 seconds

    print("YOU BLASTED ", S, "/10 BUGS")
    exit(1)

main()
# 213