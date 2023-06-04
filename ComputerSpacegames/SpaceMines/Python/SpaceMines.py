import random
import os
import time

class Game:
	def __init__(self):
		"""
		Initialize the game variables.
		"""
		self.mines_count = random.randint(5, 5 + 3)
		self.people = random.randint(40, 40 + 60)
		self.money = random.randint(10, 10 + 50) * self.people
		# FP = random.randint(80, 80 + 40) # price of food is not used.
		self.tons_produced = random.randint(80, 80 + 40)
		self.ore_in_store_tons = 0
		self.satistaction_factor = 1
		self.year_count = 1

	def start_cycle(self):
		"""
		Start one yearly cycle.
		"""
		self.mine_selling_price = random.randint(2000, 2000 + 2000)
		self.ore_selline_price = random.randint(7, 7 + 12)
		self.calculate_or_in_store()

	def calculate_or_in_store(self):
		"""
		Calculate how much ore is stored and produced this year.
		"""
		produced_for_a_year = self.total_produced()
		self.ore_in_store_tons = self.ore_in_store_tons + produced_for_a_year
		return self.ore_in_store_tons

	def total_produced(self):
		"""
		Calculate how much ore was produced this year.
		"""
		result = self.tons_produced * self.mines_count
		return result


	def report(self):
		"""
		A yearly report of the mines's performance.
		"""
		os.system("cls")
		print("YEAR", self.year_count)
		print()

		print("SATISFACTION FACTOR", self.satistaction_factor)
		print()
		print("YOUR MINES PRODUCED ", self.tons_produced, " TONS EACH")
		print("ORE IN STORE=", self.ore_in_store_tons, " TONS")

	def sell(self):
		"""
		Execute the sell actions.
		"""
		print("SELLING")
		self.sell_ore()
		self.sell_mine()

	def sell_ore(self):
		"""
		Selling ore.
		"""
		print("ORE SELLING PRICE=", self.ore_selline_price)
		print("ORE TOTAL PRICE=", self.ore_in_store_tons * self.ore_selline_price)
		print("ORE IN STORE=", self.ore_in_store_tons, " TONS")
		
		while True:
			print("HOW MUCH ORE TO SELL?")
			or_to_sell_string = input()
			self.ore_to_sell = int(or_to_sell_string)
			if self.ore_to_sell > self.ore_in_store_tons:
				print("can not sell more ore than in store")
				continue

			if self.ore_to_sell < 0:
				print("can not sell less than 0 ore.")
				continue

			break

		self.ore_in_store_tons = self.ore_in_store_tons - self.ore_to_sell
		print("ORE LEFT IN STORE=", self.ore_in_store_tons, " TONS")

		money_made = self.ore_to_sell * self.ore_selline_price
		self.money = self.money + money_made
		print("MADE MONEY $", money_made)

	def sell_mine(self):
		"""
		Selling a mine.
		"""
		print("TOTAL MONEY $", self.money)

		print("YOU HAVE ", self.mines_count, " MINES AND $", self.money)
		print("THERE ARE ", self.people, " PEOPLE IN THE COLONY.")
		print("THERE ARE ", self.people/self.mines_count, " PEOPLE PER MINE.")
		print("There are enough people for ", int(self.people/10), " mines.")

		print("MINE SELLING PRICE=", self.mine_selling_price, "/MINE")
		print("TOTAL MINE PRICE=", self.mines_count*self.mine_selling_price)
		while True:
			print("YOU HAVE ", self.mines_count)
			print("HOW MANY MINES TO SELL?")
			self.mines_to_sell = int(input())
			if not (self.mines_to_sell < 0 or self.mines_to_sell > self.mines_count):
				break

		self.mines_count = self.mines_count - self.mines_to_sell
		mine_money = self.mines_to_sell * self.mine_selling_price
		self.money = self.money + mine_money
		print("MADE MONEY OUT OF SELLING THE MINES $", mine_money)

		print()
		print("YOU HAVE $", self.money)

	def buy(self):
		"""
		Buying food and mines.
		"""
		print()
		print("BUYING")

		self.buy_food()
		self.buy_mines()

	def buy_food(self):
		"""
		Buying food for the poeple to keep them happy.
		"""
		print("THERE ARE ", self.people, " PEOPLE IN THE COLONY.")
		print("Usually buying $", self.people*100, " food.")
		print("Poeople would be happy with $", self.people*121, " food.")

		while True:
			print("HOW MUCH TO SPEND ON FOOD ? (APPR. $100 per person.)")
			self.food_budget = int(input())
			if self.food_budget > self.money:
				print(f'Only have {self.money} money')
				continue

			if self.food_budget < 0:
				print(f'The least to buy is 0.')
				continue

			break

		self.money = self.money - self.food_budget
		print("After the food you have $", self.money)

		self.food_per_person = self.food_budget / self.people
		if self.food_per_person > 120:
			print("Satisfaction increased")
			self.satistaction_factor = self.satistaction_factor + 0.1

		if self.food_per_person < 80:
			print("Satisfaction decreased")
			self.satistaction_factor = self.satistaction_factor - 0.2
		print()

	def buy_mines(self):
		"""
		Buying mines to generate more ore.
		"""
		if self.money>=self.mine_selling_price:
			while True:
				print("YOU HAVE ", self.mines_count, " MINES AND $", self.money)
				print("THERE ARE ", self.people, " PEOPLE IN THE COLONY.")
				print("THERE ARE ", self.people/self.mines_count, " PEOPLE PER MINE.")
				print("There are enough people for ", int(self.people/10), " mines.")

				print(f"Mine price is {self.mine_selling_price}")
				print("HOW MANY MORE MINES TO BUY?")
				self.mintes_to_buy = int(input())
				price = self.mintes_to_buy * self.mine_selling_price
				if price > self.money:
					print("do not have that much money for $",price," mines")
					continue

				if price <0:
					print("can not buy less than 0 minues")
					continue

				break

			if self.mintes_to_buy>0:
				self.mines_count = self.mines_count + self.mintes_to_buy
				self.money = self.money - self.mintes_to_buy * self.mine_selling_price

		else:
			print("Not enought money yet to buy a mine.")

	def calculate_satisfaction(self):
		"""
		Calculate all the satisfaction settings.
		"""
		self.revolted = False
		self.overworked = False
		self.left = False

		self.calculate_produced()
		self.calculate_recruitment()

	def calculate_produced(self):
		"""
		Use the satisfaction factor to influence the production of ore.
		"""
		if self.satistaction_factor < 0.6:
			self.revolted = True
			return

		if self.satistaction_factor > 1.1:
			print('The people are happy, produce extra')
			self.tons_produced = self.tons_produced + random.randint(1, 1 + 20)

		if self.satistaction_factor < 0.9:
			print('The people are sad, produce less')
			self.tons_produced = self.tons_produced - random.randint(1, 1 + 20)

	def calculate_recruitment(self):
		"""
		Use the satisfaction factor to influence the recruitement of poeple.
		"""

		self.people_per_mine = self.people / self.mines_count
		if self.people_per_mine < 10:
			print(f'There is only {self.people_per_mine} people per mine. So overworked everyone.')
			self.overworked = True
			return

		if self.satistaction_factor > 1.1:
			people = self.people
			self.people = self.people + random.randint(1, 1 + 10)
			print(f'people increased from {people} to {self.people}')

		if self.satistaction_factor < 0.9:
			people = self.people
			self.people = self.people - random.randint(1, 1 + 10)
			print(f'people decreased from {people} to {self.people}')

		if self.people < 30:
			self.left = True
			return

	def major_events(self):
		"""
		There will be possible major events.
		Execute these.
		"""

		if random.random() <= 0.01:
			print("RADIOACTIVE LEAK....MANY DIE")
			self.people = int(people / 2)

		if self.tons_produced >= 150:
			print("MARGET GLUT - PRICE DROPS")
			self.tons_produced = int(self.tons_produced / 2)

	def term(self):
		"""
		Proceed to the next term.
		"""
		self.year_count = self.year_count + 1

		# Your term is 10 years:
		if self.year_count > 10:
			return True

		print('welcome to the next term')
		time.sleep(2)
		return False

def main():	
	"""
	The main entry point of the game
	"""
	game = Game()

	while True:
		if not play_one_year(game):
			break

	retire()

def play_one_year(game):
	"""
	Execute the game for one year cycle.
	"""
	game.start_cycle()

	game.report()

	game.sell()
	game.buy()

	game.calculate_satisfaction()

	if game.revolted:
		revolted()

	if game.overworked:
		overworked()
		return False

	if game.left:
		everyone_left()
		return False

	game.major_events()
	
	finished = game.term()
	if finished:
		return False

	return True

def retire():
	"""
	The player succeeded.
	"""
	print("YOU SURVIVED YOU TERM OF OFFICE")

def overworked():
	"""
	Game over, the people are overworked.
	"""
	print("YOU'VE OVERWORKED EVERYONE")
	exit(1)

def revolted():
	"""
	Game over, the people revolted.
	Say a message because the people are very unhappy.
	"""
	print("THE PEOPLE REVOLTED")
	exit(1)

def everyone_left():
	"""
	The people left
	"""
	print("NOT ENOUGH PEOPLE LEFT")
	exit(1)

main()
