from stapel import *
from user import *
class Karte():
    def __init__(self,art,wert,kartenname):
        self.art = art
        self.wert = wert
        self.kartenname = self.art + " " + self.wert
        self.possible_karte = []


    def get_kartenname(self):
        return self.kartenname
    

    
    def karte_check(self,stapel,user):
        if stapel.get_active() == 'd':
            if self.wert == '7':
                print(self.kartenname)
                user.possible_cards_append(self)
        elif stapel.get_active() == 's':
            stapel.set_active_effect(None)
            user.set_passiv()
        elif stapel.get_active() != 's':
            if self.art == stapel.last_card().art or self.wert == stapel.last_card().wert:
                    user.possible_cards_append(self)
        elif stapel.get_active() == 'a':
            print("Du musst ausetzen.")
            stapel.set_active_effect(None)
            user.set_passive()






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


    def get_effect(self):
        return self.effekt





