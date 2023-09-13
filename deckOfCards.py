import random
## import interface

class Card:
    """Card class representing a playing card, contains the name and the suit"""
    def __init__(self, name, suit, emoji=""):
        self.name = name
        self.suit = suit
        self.emoji = emoji
        
class DeckOfCards:
    """DeckOfCards class represents an deck of cards"""
    deck = []

    def __init__(self):
        nameList = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q","K"]
        suitList = ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]
        self.emojiList = ["🂡", "🂢", "🂣", "🂤","🂥","🂦", "🂧","🂨",	"🂩", "🂪",	"🂫", "🂭", "🂮", 
                      "🂱",	"🂲", "🂳", "🂴", "🂵",	"🂶","🂷", "🂸", "🂹", "🂺", "🂻", "🂽", "🂾", 
                      "🃁", "🃂", "🃃",	"🃄","🃅",	"🃆",	"🃇",	"🃈",	"🃉",	"🃊",	"🃋",	"🃍",	"🃎", 
                      "🃑", 	"🃒",	"🃓",	"🃔",	"🃕",	"🃖",	"🃗",	"🃘",	"🃙",	"🃚",	"🃛",	"🃝",	"🃞"]
        # emojiNumList = ["1", "2", "3", "4", "5", "6", "7" "8" "9", "A", "B", "D", "E"]

        count = 0
        for itemSuit in suitList:
            for itemName in nameList:
                self.deck.append(Card(itemName, itemSuit, self.emojiList[count]))
                count += 1

        # for item in self.deck: 
        #     print(item.name, item.suit, item.emoji)
        """for item in range(52): 
            self.deck[item].emoji = self.emojiList[item]
            print(self.deck[item].name, self.deck[item].suit, self.deck[item].emoji)"""

        
        

    def Shuffle(self):
        """Shuffles the cards in the deck randomly"""
        random.shuffle(self.deck)

    def Deal(self, playerCount): 
        """Deals the cards in the deck depending on the number of players"""
        dealHands = []
        dealCount = (len(self.deck) // playerCount)

        for item in range(playerCount): 
            dealHands.append([])

            for num in range(int(dealCount)): 
                dealHands[item].append(self.deck[len(self.deck)-1])
                self.deck.pop()

        return dealHands
    
    def DisplayDeck(self): 
        """Displays the cards in the deck"""
        for item in self.deck:
            print(item.name, item.suit)

class Player(DeckOfCards): 
    """Player class represents playing the game, takes an number of players"""
    scoreHand = []
    lastCard = None

    def __init__(self, numberOfPlayers): 
        DeckOfCards.__init__(self)
        
        self.numberOfPlayers = numberOfPlayers
        self.lastCard = Card("", "")

    def GetHands(self): 
        """Deals the cards out to the player hand depending on the number of players"""
        self.hands = self.Deal(self.numberOfPlayers)

        for num in range(self.numberOfPlayers): 
            self.scoreHand.append([])

    def Snap(self): 
        """Plays the Game of Snap"""
        players = self.numberOfPlayers
        centerPile = []
        ## self.scoreHand = []

        ## self.GetHands()
        rounds = 0
        while any(self.hands):
            rounds += 1
            print(f"\n#{rounds}")
            for player in range(players): 
                card = self.hands[player][len(self.hands[player])-1]
                centerPile.append(card)
                self.hands[player].pop()
                print(f"Player {player + 1} Plays an {card.name} of {card.suit}")
            
                if card.name == self.lastCard.name:
                    print(f"Player {player+1} Snap!")

                    for item in centerPile: 
                        self.scoreHand[player].append(item) 
                    centerPile.clear()
                    self.lastCard = Card("", "")
                else:
                    self.lastCard = card
        
        winner = ""
        lastHand = 0
        winnerPlayer = ""
        count = 0
        for hand in self.scoreHand:
            count += 1
            if len(hand) > lastHand:
                winnerPlayer = f"Player {count}"
                winner = f"The Winner Is The Player {winnerPlayer} with {len(hand)} Cards!"
                

        print(winner)
        
    def InterfaceSnap(self): 
        """Plays the Game of Snap"""
        players = self.numberOfPlayers
        centerPile = []
        ## self.scoreHand = []

        ## self.GetHands()
        rounds = 0
        while any(self.hands):
            rounds += 1
            print(f"\n#{rounds}")
            for player in range(players): 
                card = self.hands[player][len(self.hands[player])-1]
                centerPile.append(card)

                self.hands[player].pop()
                print(f"Player {player + 1} Plays an {card.name} of {card.suit}")
            
                if card.name == self.lastCard.name:
                    print(f"Player {player+1} Snap!")

                    for item in centerPile: 
                        self.scoreHand[player].append(item) 
                    centerPile.clear()
                    self.lastCard = Card("", "")
                else:
                    self.lastCard = card
        
        winner = ""
        lastHand = 0
        winnerPlayer = ""
        count = 0
        for hand in self.scoreHand:
            count += 1
            if len(hand) > lastHand:
                winnerPlayer = f"Player {count}"
                winner = f"The Winner Is The Player {winnerPlayer} with {len(hand)} Cards!"
                

        print(winner)

def main(): 
    print(f"hello")
    pass

if __name__ == "__main__": 
    main()






            
        





    
