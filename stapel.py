from karten import *
import random as r
class Ziehstapel():
    def __init__(self,deck):
        self.deck = deck
        self.rest = []
        r.shuffle(self.deck)
        self.active_effect = None
        self.wish = None

    def last_card(self):
        return self.rest[len(self.rest)-1]
    
    def draw_cards(self,user,amount):
        print(len(self.deck)-amount)
        if (len(self.deck)-1) <= amount:
            lastcard = self.rest[(len(self.rest)-1)]
            print(lastcard)
            self.deck = r.shuffle(self.rest)
            self.rest.append(lastcard)
    
        
        i = 0
        while i <= amount:
            user.add_card(self.deck.pop(0))
            i += 1

    def frist_draw_cards(self,user,amount):
        i = 0
        while i <= amount:
            user.add_card(self.deck.pop(0))
            i += 1

    def card_put_down(self,card,user):
        print(card)
        self.rest.append(card)
        user.set_passive()
    
    def first_card_down(self):
        self.rest.append(self.deck.pop(0))

    def last_card(self):
        return self.rest[len(self.rest)-1]
    
    def set_wish(self,wish):
        self.wish = wish

    def set_active_effect(self,kind):
            self.active_effect = kind

    def get_active(self):
        return self.active_effect

    
