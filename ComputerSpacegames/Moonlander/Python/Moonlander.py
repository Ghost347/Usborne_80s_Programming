import os
os.system("cls")
print("MOONLANDER")
time_spent = 0
height = 500
velocity_current = 0
velocity_average = 0
velocity_final = 0
fuel_left = 500

while True:
	print("TIME", time_spent, "	", "HEIGHT", height)
	print("VEL.", velocity_current, "	", "FUEL", fuel_left)
	if fuel_left != 0:
		print("BURN? (0-30)")
		burn = 0
		burn_input = input()

		if burn_input!='':
			burn = int(burn_input)

		if burn < 0:
			burn = 0

		if burn > 30:
			burn = 30

	if burn > fuel_left:
		burn = fuel_left

	velocity_next = velocity_current - burn + 5
	fuel_left = fuel_left - burn
	velocity_average = (velocity_next + velocity_current) / 2
	if velocity_average >= height:
		break

	height = height - velocity_average
	time_spent = time_spent + 1
	velocity_current = velocity_next

velocity_final = velocity_current + (5 - burn) * height / velocity_current
print(f'final velocity : {velocity_final}')
if velocity_final > 5:
	print("YOU CRASHED-ALL DEAD")

if velocity_final > 1 and velocity_final <= 5:
	print("OK-BUT SOME INJURIES")

if velocity_final <= 1:
	print("GOOD LANDING.")
    
exit(1)
