import Suits

class Card:
	suit = Suits.Suit()
	number = int()

	def __init__(self, suit, number):
		self.suit 	= suit
		self.number = number