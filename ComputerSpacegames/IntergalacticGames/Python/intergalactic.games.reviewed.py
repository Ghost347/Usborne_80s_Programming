import random
import math

def launch_satellite():
    print("YOU'VE DONE IT")
    print("NCTV WINS-THANKS TO YOU")
    exit(1)

print("INTERGALACTIC GAMES")
H = random.randint(1, 100)
print("YOU MUST LAUNCH A SATELLITE")
print("TO A HEIGHT OF", H)

for i in range(8):
    print(f"ATTEMPT #{i+1}")
    angle = int(input("ENTER ANGLE (0-90): "))
    speed = int(input("ENTER SPEED (0-40000): "))

    adjusted_angle = angle - math.degrees(math.atan(H / 3))
    adjusted_speed = speed - 3000 * math.sqrt(H + 1 / H)

    if abs(adjusted_angle) < 2 and abs(adjusted_speed) < 100:
        launch_satellite()
    else:
        if adjusted_angle < -2:
            print("TOO SHALLOW")
        elif adjusted_angle > 2:
            print("TOO STEEP")
        if adjusted_speed < -100:
            print("TOO SLOW")
        elif adjusted_speed > 100:
            print("TOO FAST")

print("YOU'VE FAILED")
print("YOU'RE FIRED")
exit(1)
