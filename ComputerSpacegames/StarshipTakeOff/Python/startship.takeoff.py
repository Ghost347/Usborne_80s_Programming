import os
import random
def successful_takeoff():
	print("GOOD TAKE OFF")
	exit(1)

os.system("clear")
print("STARSHIP TAKE-OFF")
G = random.randint(1, 20)
W = random.randint(1, 40)
R = G * W
print("GRAVITY= ", G)
print("TYPE IN FORCE")
for C in range(1, 10+1):
	F = int(input())
	if F > R:
		print("TOO HIGH", end="")
	if F < R:
		print("TOO LOW", end="")
	if F == R:
		successful_takeoff()
	if C != 10:
		print(", TRY AGAIN")
print()
print("YOU FAILED =")
print("THE ALIENS GOT YOU")
exit(1)
