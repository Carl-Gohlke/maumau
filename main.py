from stapel import *
from karten import *
from user import *
import time as t

#predefinitionen

arten = ['Herz','Karo','Pik','Kreuz']
werte = ['7','8','9','10','B','D','K','A']
deck = []
user = []
rangliste = []






#funktionen

def game():
    i = 0
    sieben = 0
    while len(user) >= 2:
        user[i].set_active()
        while user[i].get_status():
            if new_stapel.get_active() != 'd':
                if new_stapel.get_active() != 'a':
                    print(f"{user[i].get_name()} ist dran.")
                    print(f"Oberste Karte: {new_stapel.last_card().get_kartenname()}")
                    user[i].possible_cards_clear()
                    for karte in user[i].get_hand():
                        karte.karte_check(new_stapel,user[i])
                    if len(user[i].get_possbile_cards()) == 0:
                        new_stapel.draw_cards(user[i],1)
                        print("Du kannst keine Karte legen.\nDu hast eine Karte gezogen.\nDer nächste Spieler ist dran.")
                        user[i].set_passive()
                    else:
                        print(f"Deine Hand:\n")
                        for o in user[i].get_hand():
                            print(o.get_kartenname())
                        print("Du kannst folgende Karten legen:\n")
                        counter = 1
                        for b in user[i].get_possbile_cards():
                            print(f"Nr.{counter} {b.get_kartenname()}")
                            counter +=1
                        user[i].choosecard(new_stapel)
                        if len(user[i].get_hand()) == 0:
                            rangliste.append(user[i])
                            user.remove(user[i])
                else:
                    user[i].set_passive()
                    new_stapel.set_active_effect(None)
                    break
            else:
                sieben += 1
                print(f"{user[i].get_name()} ist dran.")
                print(f"Oberste Karte: {new_stapel.last_card().get_kartenname()}")
                user[i].possible_cards_clear()
                for karte in user[i].get_hand():
                    karte.karte_check(new_stapel,user[i])
                if len(user[i].get_possbile_cards()) == 0:
                    new_stapel.draw_cards(user[i],sieben*2)
                    print(f"Du hast keine 7 du musst {sieben*2} Karten ziehen.")
                    user[i].set_passive()
                    new_stapel.set_active_effect(None)
                else:
                    print(f"Deine Hand:\n")
                    for o in user[i].get_hand():
                        print(o.get_kartenname())
                    print("Du kannst folgende Karten legen:\n")
                    counter = 1
                    for b in user[i].get_possbile_cards():
                        print(f"Nr.{counter} {b.get_kartenname()}")
                        counter +=1
                    user[i].choosecard(new_stapel)
                    if len(user[i].get_hand()) == 0:
                        rangliste.append(user[i])
                        user.remove(user[i])
            i+=1
            if i == len(user): 
                i = 0

             






    if len(user) <= 1:
        rangliste.append(user[0])
        print("Das Spiel ist zu Ende.")
        for c in range(0,len(rangliste)):
            print(f"Platz: {c+1}) rangliste{c}")

            


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
        new_stapel.frist_draw_cards(nutzer,spielkarten_anzahl)
    new_stapel.first_card_down()
    game()

    

def draw_card(spielkarten_anzahl):
    for nutzer in user:
        new_stapel.draw_cards(nutzer,spielkarten_anzahl)

def game_start():
    anzahl_spielkarten = int(input("Spielkartenanzahl: \n"))-1
    if len(arten) * len(werte) <= anzahl_spielkarten * len(user):
        print(f"E R R O R\n Zu wenig Karten im Spielblatt\nJeder Spieler kann maximl {int(31/len(user))} Karten haben")
        game_start()
    else: 
        first_austeilen(anzahl_spielkarten)

        
        

player_count = int(input("Spieleranzahl:\n"))
gen_user(player_count)
gen_karten()
new_stapel = Ziehstapel(deck)

game_start()
t.sleep(30)



