import Cards

class Input:
	opponentCard = Cards.Card()
	dealerCard   = [Cards.Card]()

	def __init__(self, opponentCard, dealerCard):
		self.opponentCard = opponentCard
		self.dealerCard   = dealerCard