from karten import *
import random as r
class Ziehstapel():
    def __init__(self,deck):
        self.deck = deck[:]
        self.rest = []
        r.shuffle(self.deck)
        self.active_effect = None
        self.wish = None

    def last_card(self):
        return self.rest[-1]
    
    def draw_cards(self,user,amount):
        if (len(self.deck)) <= amount:
            lastcard = self.rest[-1]
            self.deck = self.rest[:]
            r.shuffle(self.deck)
            self.rest = [lastcard]
        else:   
            for i in range(amount):
                user.add_card(self.deck.pop(0))

    def first_draw_cards(self,user,amount):
        for _ in range(amount):
            user.add_card(self.deck.pop(0))

    def card_put_down(self,card,user):
        self.rest.append(card)
        user.set_passive()
        
    
    def first_card_down(self):
        self.rest.append(self.deck.pop(0))
    
    def set_wish(self,wish):
        self.wish = wish

    def set_active_effect(self,kind):
            self.active_effect = kind

    def get_active(self):
        return self.active_effect

    
