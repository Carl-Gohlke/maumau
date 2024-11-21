class Karte():
    def __init__(self,art,wert):
        self.art = art
        self.wert = wert
    
    


class Spezialkarte(Karte):
    def __init__(self,art,wert,effekt):
        super().__init__(art,wert)
        self.effekt = effekt

    def getInfo(self):
        if self.effekt == "None":
            return self.art,self.wert
        else:
            return self.art, self.wert, self.effekt
    
    def getArt(self):
        return self.art
    
    def getWert(self):
        return self.wert

    def getEffect(self):
        return self.effekt