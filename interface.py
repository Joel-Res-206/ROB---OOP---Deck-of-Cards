import tkinter as tk
from deckOfCards import Card, DeckOfCards, Player
import time

players = 5

def StartGame(event):
    play = Player(players)

    play.Shuffle()
    play.GetHands()

    play.Snap = InterfaceSnap

    play.Snap(play)


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

                # interface
                for item in labelList: 
                    item["foreground"] = "black"
                    item["text"] = f"🂠"

                labelList[player]["text"] = card.emoji

                if card.suit == "DIAMONDS" or card.suit == "HEARTS": 
                    labelList[player]["foreground"] = "red"
                else:
                    labelList[player]["foreground"] = "black"

                window.update()
                
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
                    centerLabel["text"] = card.emoji

                    if card.suit == "DIAMONDS" or card.suit == "HEARTS": 
                        centerLabel["foreground"] = "red"
                    else: 
                        centerLabel["foreground"] = "black"

                time.sleep(2)
        
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
        

labelList = []

window = tk.Tk()

frame1 = tk.Frame()
frame1.pack()

for item in range(players): 
    label = tk.Label(master=frame1, text=f"🂠", font=("Arial", 150))
    labelList.append(label)

for item in labelList: 
    item.pack(side="left")

frame2 = tk.Frame()
frame2.pack()

centerLabel = tk.Label(master=frame2, text="Card", font=("Arial", 152))
centerLabel.pack(pady=20)

frame3 = tk.Frame()
frame3.pack()

button = tk.Button(master=frame3, text="Start")
button.pack(padx=15)

button.bind("<Button-1>", StartGame)

window.mainloop()