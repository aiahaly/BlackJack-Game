#https://www.youtube.com/watch?v=AaSiArXGtfs
#https://github.com/JabrahTutorials/ReinforcementLearning/blob/master/BlackJackMonteCarlo/game.py
#https://www.youtube.com/watch?v=G7RrQW2Gu98
#https://tkdocs.com/shipman/button.html
#https://www.youtube.com/watch?v=K_TINFKl0Lw
#https://tkdocs.com/shipman/
#https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
#https://www.youtube.com/watch?v=yQSEXcf6s2I


import tkinter as tk
import random
Ranks= ['A', '2', '3','4','5','6','7','8','9','10','J','K','Q']
Values={'A': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'J':10,'Q':10, 'K':1}
window= tk.Tk()
window.title("BlackJack Game")
window.configure(background="red")
window.geometry("860x1024")

###header=tk,PhotoImage(file="") We can insert blackjack logo here if we want
dealer_hand=[]
player_hand=[]
class Deck:
    def __init__(self):     #inputting widgets
        self.deck_list=[]
        global Ranks
        for r in Ranks:
            self.deck_list.append(r)

        self.start= tk.Button(window, text="Deal", width=4, command=self.deal_card)
        self.start.pack()
        self.labDealer=tk.Label(window, text="Dealer's Hand", width=13)
        self.labDealer.pack(side=tk.LEFT)
        self.labPlayer=tk.Label(window, text="Player's Hand", width=13)
        self.labPlayer.pack(side=tk.RIGHT)
        self.dealer= tk.Text(window, height=15, width=30, bg="white")
        self.player= tk.Text(window, height=15, width=30, bg="green")
    def get_deck(self): ##To return list of deck elements
        return self.deck_list
    def shuffle(self):   #shuffles deck
        return random.shuffle(self.deck_list)
    def deal_card(self):    #shuffles, removes start widget, deals cards, provides hit and end option during turns
        self.shuffle()
        self.start.destroy()
        self.deal_to_dealer()
        self.deal_to_player()
        self.deal_to_player()

        self.end=tk.Button(window, text="END TURN", width=8, command=self.end)
        self.end.pack()

        self.hit=tk.Button(window, text="HIT", width=3, command=self.hit)
        self.hit.pack()
    def end(self):
        #window.quit()
        player_score=self.get_player_score()
        dealer_score=self.get_dealer_score()
        if (player_score > dealer_score):
            print ("Dealer score:", dealer_score)
            print ("Player score:", player_score)
            print("You win")
        elif(player_score == dealer_score):
            print ("Dealer score:", dealer_score)
            print ("Player score:", player_score)
            print("Draw")
        else:
            print ("Dealer score:", dealer_score)
            print ("Player score:", player_score)
            print("You lose")
        #window.destroy()
    def hit(self):       #allows hit to deal to player
        self.deal_to_player()
    def deal_to_dealer(self):      #allows hit to deal to dealer
        dealer_hand.append(self.deck_list.pop(0))
        self.dealer.pack(side=tk.LEFT)
        self.dealer.delete('1.0',tk.END)
        self.dealer.insert(tk.END, dealer_hand) # shows only the first card and hides the second

        dealer_score=self.get_dealer_score()    #function to keep track of when 17 is reaced by dealer
        while (dealer_score<17):
            dealer_hand.append(self.deck_list.pop(0))
            dealer_score=self.get_dealer_score()
            if dealer_score > 21:
                #window.quit()
                print("Dealer Busted")
                print("YOU WIN")
                #window.destroy() <17 keep hitting can only stand if >17
    def deal_to_player(self):       #prints results, meant to deal new cards to players when they press hit
        player_hand.append(self.deck_list.pop(0))
        self.player.pack(side=tk.RIGHT)
        self.player.delete('1.0',tk.END)
        self.player.insert(tk.END, player_hand)

        if (self.get_player_score()>21):
            window.quit()
            print("Your Busted")
            print ("You Lose")
            #window.destroy()
    def get_player_score(self):
        player_value=0
        for card in player_hand:
            player_value += Values.get(card, 0)
        return player_value
    def get_dealer_score(self):
        dealer_value=0
        for card in dealer_hand:
            dealer_value += Values.get(card, 0)
        return dealer_value
if __name__ == '__main__':      #meant to run the file only if the file is run directly without anything being imported.
    d=Deck()
    window.mainloop()
