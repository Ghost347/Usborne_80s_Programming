import random
import msvcrt


def main():
	"""
	The main function.
	"""
	cave_width = intro()
	game = Game(cave_width)

	while True:
		if execute_one_game_cycle(game):
			break
		
	if game.success:
		success()

def intro():
	"""
	Introduce the game.
	"""
	print("DEATH VALLEY")
	print("WIDTH?")
	cave_width = int(input())
	return cave_width

class Game:
	def __init__(self, cave_width):
		"""
		Initialize the game:
		"""
		self.size = 10.0
		self.cave_progress = 0
		self.cave_width = float(cave_width / 2.0) * self.size
		self.cave_progress = 0
		self.cave_length = 400000
		self.left_wall = 10* self.size
		self.right_wall = self.cave_width*2
		self.max_wall = self.right_wall*1.2
		self.max_wall = 100*self.size
		self.Y = (self.left_wall + self.right_wall) /2

		self.count = 0
		self.ending = False
		self.shape = Shape()
		self.success = False

	def adjust_wall(self):
		"""
		Create a new slice of the wall.
		"""
		self.shape.execute(self)

	def view(self):
		"""
		Must the line be viewed.
		"""
		if (self.count % 1000) == 1:
			return True

		return False

	def left(self):
		"""
		Return the left value on the display.
		"""
		result = int(self.left_wall /self.size)
		return result

	def me(self):
		"""
		Return the player value on the display.
		"""
		result = int(self.Y /self.size)
		return result

	def right(self):
		"""
		Return the right value on the display.
		"""
		result = int(self.right_wall /self.size)
		return result

	def crashed(self):
		"""
		Verify if the player crashed.
		"""
		if self.Y<self.left_wall:
			self.ending = True
			self.success = False
			return True

		if self.Y>self.right_wall:
			self.ending = True
			self.success = False
			return True

		return False

	def progress(self):
		"""
		Keep track of the progress in the tunnel.
		"""
		self.cave_progress = self.cave_progress + 1
		if self.cave_progress < self.cave_length:
			return

		self.ending = True
		self.success = True

	def end(self):
		"""
		Indicate if the game is already over.
		"""
		return self.ending

	def go_left(self):
		"""
		The player pressed the left key. So go left.
		"""
		self.Y = self.Y - self.size
		self.right_wall = self.right_wall + 1


	def go_right(self):
		"""
		The player pressed the right key. So go right.
		"""
		self.Y = self.Y + self.size
		self.right_wall = self.right_wall - 1

class Shape:

		

	# =======================================================================================
	def __init__(self):
		"""
		Initialize the shape of the wall.
		"""
		self.momentum = 0
		self.angle = 0
		self.value = 0

	def execute(self, game):
		"""
		Execute one step in the wall:
		"""
		self.momentum -=1
		if self.momentum <=0:
			return self.start_angle(game)

		game.left_wall += self.value
		game.right_wall += self.value
		self.value += self.angle

		if game.left_wall < game.size:
			game.left_wall = game.size
			return self.start_angle(game)

		if game.right_wall > game.max_wall:
			game.right_wall = game.max_wall
			return self.start_angle(game)

	def start_angle(self, game):
		"""
		Start with a new angle in the cave.
		"""
		# random numbers for all three:
		# value = float(random.random() * (3.0) - (1.5))
		# value = float(random.random() * (0.6) - (0.3))

		self.value = float(random.random() * 3.0 - 1.5)*game.size/200000
		self.angle = float(random.random() * 0.4 - 0.2)*game.size/300000
		self.momentum = random.random() * (10000*game.size)
		
def execute_one_game_cycle(game):
	"""
	Execute one complete game cycle.
	"""
	game.count = game.count + 1

	game.adjust_wall()

	view(game)

	process_input(game)

	if game.crashed():
		game_over(game)

	game.progress()

	if game.end():
		return True

	return False

	if not (cave_progress < cave_length):
		return left_wall,right_wall,cave_progress,True,Y,count,True

	return left_wall,right_wall,cave_progress,False,Y,count,True


def view(game):
	"""
	Draw the player and the tunnel.
	"""
	if not game.view():	
		return

	left = game.left()
	me = game.me()
	right = game.right()
	left_view = left
	right_view = right - me
	me_view = me - left
	print(" " * left_view , "I", " " * me_view , "*", " " * right_view , "I")

def process_input(game):
	"""
	Process the keyboard input.
	"""
	if not msvcrt.kbhit():
		return

	keyboard_key = get_input()

	if keyboard_key == "Q":
		game.go_left()

	if keyboard_key == "q":
		game.go_left()

	if keyboard_key == "P":
		game.go_right()

	if keyboard_key == "p":
		game.go_right()


def get_input():
	"""
	Fetch an appropriate key from the keyboard.
	"""
	if msvcrt.kbhit():
		ch = msvcrt.getch()
		result = ch.decode('ascii')
		return result

	return ''

def game_over(game):
	"""
	Report that the player failed flying through the Death Valley.
	"""
	print(game.cave_progress)
	print("YOU CRASHED INTO THE WALL")
	print("AND DISINTEGRATED")
	game.ending = True

def success():	
	"""
	Report that the player made it throught the Death Valley.
	"""
	print("WELL DONE-YOU MADE IT")
	print("THROUGH DEATH VALLEY")

main()

