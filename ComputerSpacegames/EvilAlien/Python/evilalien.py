import os
import random

def function_300():
	print("*BOOM* YOU GOT HIM!")
	exit(1)

os.system("clear")
print("EVIL ALIEN")
S = 10
G = 40
X = random.randint(0, S)
Y = random.randint(0, S)
D = random.randint(0, S)
for I in range(1, (G)+1):
	print("X POSITION (0 TO 9)?")
	X1 = int(input())
	print("Y POSITION (0 TO 9)?")
	Y1 = int(input())
	print("DISTANCE (0 TO 9)?")
	D1 = int(input())
	if X == X1 and Y == Y1 and D == D1:
		function_300()
	print("SHOT WAS ", end="")
	if Y1 > Y:
		print("NORTH", end="")
	if Y1 < Y:
		print("SOUTH", end="")
	if X1 > X:
		print("EAST", end="")
	if X1 < X:
		print("WEST", end="")
	print()
	if D1 > D:
		print("TOO FAR", end="")
	if D1 < D:
		print("NOT FAR ENOUGH", end="")

	print()

print("YOUR TIME HAS RUN OUT!!")
exit(1)

