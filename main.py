#imports
from user import User
from karten import *
from stapel import Stapel
import time
import random

#Variablen
blatt = []
user = []
min_user = 2
max_user = 6
amountplaycards = 0

#Karten Gen

def kartengen():
    art = ["Kreuz","Pik", "Karo", "Herz"]
    wert = ["7","8","9","10","B","D","K","A"]
    effekt = ["skip","wish","draw"]
    for i in art:
        for u in wert:
            if u == 7:
                new_karte = Spezialkarte(i,u,effekt[2])
                blatt.append(new_karte)
            elif u == "B":
                new_karte = Spezialkarte(i,u,effekt[1])
                blatt.append(new_karte)
            elif u == "A":
                new_karte = Spezialkarte(i,u,effekt[0])
                blatt.append(new_karte)
            else:
                new_karte = Spezialkarte(i,u,"None")
                blatt.append(new_karte)




            
            






#Spieler Gen

def spielergen():
    anzahl_user = int(input("Spieleranzahl (min.2 | max. 8):\n"))
    if anzahl_user >= min_user and anzahl_user <= max_user:
        for i in range(0,anzahl_user):
            name = input(f"Spieler {i+1}) Name:\n")
            new_user = User(name)
            user.append(new_user)
    else:
        print("E R R O R\nSpielergeneration begint von vorne\n.\n..\n...")
        time.sleep(5)
        for u in range(0,1000):
            print("\n")
        spielergen()
    random.shuffle(user)


#Spielfunktionen
def startgame(stapel):
    for i in range(0,1000):
        print("\n")
    print("Das ist die Reinfolge")
    for u in range(0,len(user)):
        print(f"{u+1}) {user[u].getName()}")
    print("Das Spiel beginnt in 5 sek.")
    for a in range(0,4):
        punkt = "."
        print(punkt*(a+1))
        time.sleep(1)
    for c in range(0,1000):
        print("\n")

    
    for b in range(0,len(user)):
        user[b].setactive()
        while user[b].getstatus() == True:
            print(f"Aktive Karte: {stapel.currentcard().getInfo()}")
            user[b].allgemeincheck(stapel)
            if b == len(user):
                b = 0

    







def amountcards(stapel):
    amountplaycards = int(input("Mit wie vielen Karten soll gespielt werden?\n"))
    if len(user) * amountplaycards >= len(blatt):
        print("E R R O R\nZu wenig Karten im Blatt\nBitte erneut eingeben")
        amountcards()
    elif amountplaycards == 0:
        print("E R R O R\nmin. eine Karte muss jeder Spieler haben\nBitte erneut eingeben")
        amountcards()
    else:
        for i in user:
            stapel.drawcard(i,amountplaycards)


def genfuncktion():
    spielergen()
    kartengen()
    stapel = Stapel(blatt)
    amountcards(stapel)
    stapel.firstcard()
    startgame(stapel)
        



#Spielgen

genfuncktion()




