import os
import time as t
from stapel import *
from karten import *
from user import *


#predefinitionen

arten = ['Herz','Karo','Pik','Kreuz']
werte = ['7','8','9','10','B','D','K','A']
deck = []
user = []
rangliste = []



def clear_console():
    """Clears the console for better readability between turns."""
    os.system('cls' if os.name == 'nt' else 'clear')


def game():
    i = 0
    while len(user) >= 2:
        clear_console()
        print(f"\nSpieleranzahl: {len(user)} | Aktive Spieler: {[u.get_name() for u in user]}")
        user[i].set_active()
        
        while user[i].get_status():
            print(f"{user[i].get_name()} ist dran.\n")
            print(f"Oberste Karte: {new_stapel.last_card().get_kartenname()}\n")
            
            user[i].possible_cards_clear()

            if new_stapel.get_active() == 'd':
                sieben +=1
            else:
                sieben = 0

            if new_stapel.get_active() == 'd':
                user[i].possible_cards_clear()
                karte.karte_check(new_stapel, user[i])

                if len(user[i].get_possible_cards()) == 0:
                    print(f"Du hast keine 7. Du musst {sieben*2} Karten ziehen.")
                    new_stapel.draw_cards(user[i], 1)
                    new_stapel.set_active_effect(None)
                    user[i].set_passive()
                    t.sleep(2)
                    continue

            elif new_stapel.get_active() == 'a':
                print("Du musst aussetzen.")
                user[i].set_passive()
                new_stapel.set_active_effect(None)
                break

            
            for karte in user[i].get_hand():
                karte.karte_check(new_stapel, user[i])
            
            if len(user[i].get_possible_cards()) == 0:
                print("Du kannst keine Karte legen. Ziehe eine Karte.")
                new_stapel.draw_cards(user[i], 1)
                user[i].set_passive()
                t.sleep(2)
                continue

            
            print("Deine Hand:")
            for idx, karte in enumerate(user[i].get_hand(), start=1):
                print(f"{idx}. {karte.get_kartenname()}")
            
            print("\nMögliche Karten:")
            for crd in user[i].get_possible_cards():
                lastcard = new_stapel.last_card()
                if lastcard.get_wert() == 'B' and crd.get_wert() == 'B':
                    user[i].remove_possible_card(crd)
            for idx, karte in enumerate(user[i].get_possible_cards(), start=1):
                print(f"{idx}. {karte.get_kartenname()}")

            user[i].choosecard(new_stapel)
            
            if len(user[i].get_hand()) == 0:
                print(f"\n{user[i].get_name()} hat gewonnen!")
                rangliste.append(user[i])
                user.pop(i)
                t.sleep(2)
                break

        print(f"\nZug von {user[i].get_name()} ist beendet.")
        print("Der nächste Spieler ist in 4 Sekunden dran...")
        t.sleep(4)
        
        i += 1
        if i >= len(user):
            i = 0

    clear_console()
    print("Das Spiel ist zu Ende.")
    print("Rangliste:")
    for platz, spieler in enumerate(rangliste, start=1):
        print(f"Platz {platz}: {spieler.get_name()}")
    print("Spiel beendet. Vielen Dank fürs Spielen!")

             






    if len(user) <= 1:
        rangliste.append(user[0])
        print("Das Spiel ist zu Ende.")
        for c in range(len(rangliste)):
            print(f"Platz {c+1}: {rangliste[c].get_name()}")

            


#genfunktionen
def gen_karten():
    for art in arten:
        for wert in werte:
            if wert == 'B':
                kartenname = art + " " + wert
                new_specialcard = Spezialkarte(art,wert,kartenname,'w')
                deck.append(new_specialcard)
            elif wert == 'A':
                kartenname = art + " " + wert
                new_specialcard = Spezialkarte(art,wert,kartenname,'a')
                deck.append(new_specialcard)
            elif wert == '7':
                kartenname = art + " " + wert
                new_specialcard = Spezialkarte(art,wert,kartenname,'d')
                deck.append(new_specialcard)
            else:
                kartenname = art + " " + wert
                new_card = Karte(art,wert,kartenname)
                deck.append(new_card)


    

def gen_user(player_count):
    print("Geben sie die Namen ein\n")
    for i in range(0,player_count):
        name = input(f"Nutzer {i+1}: \n")
        new_user = User(name)
        user.append(new_user)

#spielaufbau

def first_austeilen(spielkarten_anzahl):
    for nutzer in user:
        new_stapel.first_draw_cards(nutzer,spielkarten_anzahl)
    new_stapel.first_card_down()
    game()

    

def draw_card(spielkarten_anzahl):
    for nutzer in user:
        new_stapel.draw_cards(nutzer,spielkarten_anzahl)

def game_start():
    anzahl_spielkarten = int(input("Anzahl der Startkarten pro Spieler: "))
    if len(arten) * len(werte) < (anzahl_spielkarten * len(user)) + 1:
        print("E R R O R: Zu wenig Karten im Deck.")
        return game_start()

    print("\nKarten werden verteilt...")
    t.sleep(2)
    first_austeilen(anzahl_spielkarten)
        
        

player_count = int(input("Spieleranzahl:\n"))
gen_user(player_count)
gen_karten()
new_stapel = Ziehstapel(deck)

game_start()
t.sleep(30)



