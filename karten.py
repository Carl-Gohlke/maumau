from stapel import *
from user import *
class Karte():
    def __init__(self,art,wert,kartenname):
        self.art = art
        self.wert = wert
        self.kartenname = kartenname
        self.possible_karte = []


    def get_kartenname(self):
        return self.kartenname
    
    def karte_check(self,stapel,user):
        if self.art == stapel.last_card().art or self.wert == stapel.last_card().wert:
            if self.wert == 'B'and stapel.last_card().wert == 'B':
                pass
            else:
                user.possible_cards_append(self)

    def get_art(self):
        return self.art
    
    def get_wert(self):
        return self.wert
    
    def set_art(self,art):
        self.art = art
    
    def set_wert(self,wert):
        self.wert = wert



class Spezialkarte(Karte):
    def __init__(self,art,wert,kartenname,effekt):
        super().__init__(art,wert,kartenname)
        self.effekt = effekt






