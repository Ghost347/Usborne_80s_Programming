import os
import random
import math

def main():
	time_in_years = introduction()

	speed_of_ship, distance_of_trip = get_user_input()

	time_of_flight,time_into_future = calculate_results(speed_of_ship, distance_of_trip)
	
	report_results(time_of_flight,time_into_future, time_in_years)

def introduction():
	os.system("cls")
	print("TRIP INTO THE FUTURE")
	time_in_years = random.randint(25, 25 + 100)
	print("YOU WISH TO RETURN ", time_in_years)
	print("YEARS IN THE FUTURE.")
	print()

	return time_in_years

def get_user_input():

	while True:
		print("SPEED OF SHIP (0-1)")
		speed_of_ship = float(input())

		if speed_of_ship <= 1.0 and speed_of_ship > 0.0:
			break

	print("DISTANCE OF TRIP")
	distance_of_trip = int(input())
	return speed_of_ship, distance_of_trip

def calculate_results(speed_of_ship, distance_of_trip):
	speed_of_ship = float(speed_of_ship)
	distance_of_trip = float(distance_of_trip)

	time_of_flight = distance_of_trip / speed_of_ship
	if speed_of_ship==1.0:
		root = 0.00001
	else:
		root = math.sqrt(1.0 - speed_of_ship * speed_of_ship)
	time_into_future = time_of_flight / root

	return time_of_flight,time_into_future

def report_results(time_of_flight,time_into_future, time_in_years):
	print("YOU TOOK ", time_of_flight, " YEARS")
	print("AND ARRIVED ", time_into_future, " YEARS")
	print("IN THE FUTURE.")

	if time_of_flight > 50:
		print("YOU DIED ON THE WAY")
		return

	if abs(time_in_years - time_into_future) <= 5:
		print("YOU ARRIVED ON TIME")
		return

	if abs(time_in_years - time_into_future) > 5:
		print("NOT EVEN CLOSE")


main()