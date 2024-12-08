class User():
    def __init__(self,name):
        self.name = name
        self.hand = []
        self.possible_cards = []
        self.active = False

    def set_active(self):
        self.active = True
    
    def set_passive(self):
        self.active = False

    def get_status(self):
        return self.active

    def possible_cards_append(self,card):
        self.possible_cards.append(card)

    def get_possible_cards(self):
        return self.possible_cards
    
    def remove_possible_card(self,card):
        self.possible_cards.remove(card)
    
    def add_card(self,card):
        self.hand.append(card)

    def get_hand(self):
        return self.hand
    
    def get_name(self):
        return self.name
    
    def makewisch(self,stapel,card):
        arten = ['Herz','Karo','Pik','Kreuz']
        print(f"Wählen sie eine Art.\n")
        for art in arten:
            print(art)
        choose = input()
        self.hand.remove(self.possible_cards[card])
        self.possible_cards[card].set_art(choose)
        self.possible_cards[card].set_wert('0')
        stapel.set_active_effect(stapel.set_active_effect(self.possible_cards[card].get_effect()))
        stapel.card_put_down(self.possible_cards.pop(card),self)
        stapel.set_wish(choose)

        
    
    def choosecard(self,new_stapel):
        card = int(input("Wählen sie eine Karten Nr. aus:\n"))-1
        if self.possible_cards[card].get_wert() == 'B':
            self.makewisch(new_stapel,card)
        elif self.possible_cards[card].get_wert() == '7':
            self.hand.remove(self.possible_cards[card])
            new_stapel.set_active_effect(self.possible_cards[card].get_effect())
            new_stapel.card_put_down(self.possible_cards.pop(card),self)
        elif self.possible_cards[card].get_wert() == 'A':
            self.hand.remove(self.possible_cards[card])
            new_stapel.set_active_effect(self.possible_cards[card].get_effect())
            new_stapel.card_put_down(self.possible_cards.pop(card),self)
        else: 
            self.hand.remove(self.possible_cards[card])
            new_stapel.card_put_down(self.possible_cards.pop(card),self)
            new_stapel.set_active_effect(None)
        
    
    def possible_cards_clear(self):
        self.possible_cards = []


