import Cards
import Suits
import Input

def getInput() -> Input.Input:
	userInput = input("Enter input: ").replace(" ", "")

	inputArray = userInput.split(",")

	if len(inputArray) != 13: exit()

	classInput = Input.Input()

	
def findCard(inputArray: [str], index: int) -> Cards.Card:

	suit = Suits.Suit()

	