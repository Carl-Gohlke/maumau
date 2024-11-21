import random 
from karten import *

class Stapel():
    def __init__(self,blatt):
        self.blatt = blatt
        self.rest = []
        self.lastplayedcard = ""
        self.lastplayedcardactiv = False
        self.wish = ""
        for i in range(0,10):
            random.shuffle(self.blatt)

    def currentcard(self):
        return self.lastplayedcard

    def currenteffect(self):
        return self.lastplayedcard.getEffect()

    def drawcard(self,player,amount):
        cards = []

        for i in range(0,amount):
            cards.append(self.blatt[i])
        for u in range(amount,0):
            self.blatt.remove(u)
        
        player.addCards(cards)

    def putdown(self,card):
        self.lastplayedcard = card
        self.rest.append(card)

    def special(self):
        self.lastplayedcard = False
    
    def wish(self,art):
        self.currentcard().art = art

    def newmix(self):
        random.shuffle(self.rest)
        self.blatt = []
        self.blatt = self.rest
        self.rest = []
    
    def firstcard(self):
        self.lastplayedcard = random.choice(self.blatt)
        self.rest.append(self.lastplayedcard)
        self.blatt.remove(self.lastplayedcard)
    



