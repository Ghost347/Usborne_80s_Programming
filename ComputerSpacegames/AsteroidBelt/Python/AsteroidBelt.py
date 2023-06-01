import os
import random
import time
import msvcrt
#import msvcrt

def main():
	os.system("cls")
	print("ASTEROID BELT")
	print("Guess how big are the Asteroids.")
	time.sleep(2)

	score = 0
	for game_count in range(0, 10):
		score = play_one_game(score)
		
	print("YOU HIT ", score, " OUT OF 10")

def play_one_game(score):
	horizontal_position = random.randint(1, 19)
	vertical_position = random.randint(1, 13)
	asteroid_count = random.randint(1, 9)

	render_asteroid(horizontal_position, vertical_position, asteroid_count)

	score = get_player_input(score, asteroid_count)

	return score

def render_asteroid(horizontal_position, vertical_position, asteroid_count):
	os.system("cls")
	for count in range(0, vertical_position):
		print()
	
	# Render asteroid_count amount of stars:
	for count in range(0, asteroid_count):
		if count == 0 or count == 3 or count == 6:
			print()
			print(" " * horizontal_position , end="")

		print("*", end="")
	
	print()

def get_player_input(score, asteroid_count):
	# Wait for a key press:

	for count in range(1, 100000):
		input_text =get_input()
		if len(input_text) < 1:
			continue

		keyboard_answer = int(input_text)
		return validate_key_pressed(score, keyboard_answer, asteroid_count)
	
	print("CRASHED INTO ASTEROID")
	time.sleep(0.5)

	return score

def get_input():
    if msvcrt.kbhit():
        ch = msvcrt.getch()
        result = ch.decode('ascii')
        return result

    return ''

def validate_key_pressed(score,  keyboard_answer,  asteroid_count):
	if keyboard_answer == asteroid_count:
		print("YOU DESTROYED IT")
		score = score + 1

	elif keyboard_answer < asteroid_count:
		print("NOT STRONG ENOUGH")

	elif keyboard_answer > asteroid_count:
		print("TOO STRONG")

	time.sleep(0.5)
	return score

main()