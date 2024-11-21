from karten import *
from stapel import Stapel
art = ["Kreuz","Pik", "Karo", "Herz"]
class User():
    def __init__(self,name):
        self.name = name
        self.aktiv = False
        self.gewonnen = False
        self.karten = []

    def getName(self):
        return self.name
    
    def addCards(self,cards):
        self.karten += cards
    
    def setactive(self):
        self.aktiv = True

    def getstatus(self):
        return self.aktiv
    
    def skip(self,stapel):
        self.aktiv = False
        stapel.special()
    
    def drawcheck(self, stapel):
        draw = True
        for i in self.karten:
            while draw == True:
                if i.getWert() != "7":
                    draw = True
                else:
                    draw = False
                    print("Moechten sie ziehen?\n")
                    possiblecard = i
                    check = input("Ja/Nein")
        if check.lower() == "nein":
            stapel.putdown(possiblecard)
            self.aktiv = False
        else:
            stapel.drawcard(self,2)
            self.aktiv = False
        

                    


    def choosecards(self,stapel):
        counter=0
        counterb = 0
        for i in self.karten:
            counter +=1
            print(f"Dein Karten\n {counter, i.getInfo()}")

        karte = int(input("Welche Karte wollen sie waehlen?\n"))-1
        if self.karten[karte].getArt() == stapel.currentcard().getArt():
            stapel.putdown(self.karten[karte])
            if self.karten[karte].getArt() == "B":
                for i in art:
                    counterb += 1
                    print(f"Was wuenschen sie sich?\n")
                    print(f"counterb) {i}")
                    kind = int(input()) -1
                    stapel.wish(art[kind])
            self.aktiv = False
        elif self.karten[karte].getWert() == stapel.currentcard().getWert():
            stapel.putdown(self.karten[karte])
            self.aktiv = False
        else: 
            print("Karte passt nicht bitte legen sie eine andere Karte")
            self.choosecards(stapel)


        
    def allgemeincheck(self,stapel):
        if stapel.currenteffect() == "None" or "Wish":
            check = False
            for i in self.karten:
                if i.getArt() == stapel.currentcard().getArt():
                    check = False
                elif i.getWert() == stapel.currentcard().getWert():
                    check = False
                else: 
                    check = True
                    stapel.drawcard(self,1)


            if check == False:
                self.choosecards(stapel)
        elif stapel.currentcard().getEffect() == "Skip":
            self.skip(stapel)
        elif stapel.currentcard().getEffect() == "Draw":
            self.drawcheck(stapel)



        
            
        

        
        

        

