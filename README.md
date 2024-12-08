Hier ist eine ausführliche und aktualisierte README-Datei für dein Mau-Mau-Repository basierend auf den implementierten Änderungen und der Logik, die du beschrieben hast:

---

# MauMau

Ein Python-basiertes Kartenspiel, das die Regeln des klassischen Mau-Mau-Spiels implementiert. Es unterstützt Spezialkarten wie Bube, Ass und 7, um ein authentisches Spielerlebnis zu gewährleisten.

## Inhaltsverzeichnis
- [Einleitung](#einleitung)
- [Voraussetzungen](#voraussetzungen)
- [Installation](#installation)
- [Spielregeln](#spielregeln)
- [Verwendung](#verwendung)
- [Struktur des Codes](#struktur-des-codes)
  - [Module](#module)
  - [Spezialkarten](#spezialkarten)
- [Beispielablauf](#beispielablauf)
- [Beitrag leisten](#beitrag-leisten)


---

## Einleitung

Dieses Projekt ist eine digitale Umsetzung des Kartenspiels Mau-Mau. Es bietet ein interaktives, konsolenbasiertes Spielerlebnis und umfasst die wichtigsten Spielregeln, einschließlich der Spezialkartenmechaniken wie **Bube** (Farbwunsch), **Ass** (Aussetzen) und **7** (Karten ziehen).

---

## Voraussetzungen

- **Python 3.8** oder höher
- Standard-Bibliotheken (keine zusätzlichen externen Abhängigkeiten)

---

## Installation

1. **Repository klonen**:
   ```bash
   git clone https://github.com/Carl-Gohlke/maumau.git
   cd maumau
   ```

2. **Spiel starten**:
   ```bash
   python main.py
   ```

---

## Spielregeln

1. **Ziel**: 
   - Der Spieler, der zuerst alle seine Karten ablegt, gewinnt.

2. **Kartenwerte**:
   - **Normale Karten**: Können nur auf Karten mit gleichem Wert oder gleicher Farbe gelegt werden.
   - **Spezialkarten**:
     - **Bube (B)**: Spieler wünscht sich eine Farbe. Der nächste Spieler muss eine Karte dieser Farbe legen.
     - **Ass (A)**: Der nächste Spieler muss aussetzen.
     - **7 (7)**: Der nächste Spieler muss zwei Karten ziehen. Eine **7 auf eine 7** verdoppelt die Kartenanzahl.

3. **Spielablauf**:
   - Spieler legen reihum Karten ab.
   - Wenn ein Spieler keine gültige Karte hat, muss er eine Karte vom Ziehstapel ziehen.
   - Das Spiel endet, wenn ein Spieler keine Karten mehr hat.

---

## Verwendung

Nach dem Start des Spiels wirst du durch folgende Schritte geführt:
1. Eingabe der Spieleranzahl.
2. Definition der Spielernamen.
3. Spielstart:
   - Die Spieler legen Karten gemäß den Regeln ab.
   - Bei Spezialkarten werden die entsprechenden Effekte angewendet.
   - Nach jedem Zug wird die Konsole geleert und der nächste Spieler ist an der Reihe.

---

## Struktur des Codes

### Module

- **`karten.py`**: Definiert Karten und Spezialkarten.
  - **`Karte`**: Standardkarten mit Attributen `art`, `wert` und `kartenname`.
  - **`Spezialkarte`**: Erbt von `Karte` und fügt das Attribut `effekt` hinzu (z. B. `'w'` für Farbwahl).

- **`stapel.py`**: Verwalten des Zieh- und Ablagestapels.
  - Methoden:
    - `draw_cards(user, amount)`: Lässt einen Spieler Karten ziehen.
    - `set_active_effect(kind)`: Setzt den aktuellen Effekt (z. B. `'7'` für Karten ziehen).
    - `get_active()`: Gibt den aktiven Effekt zurück.

- **`user.py`**: Verarbeitet die Spieler und ihre Aktionen.
  - Methoden:
    - `choosecard(new_stapel)`: Lässt den Spieler eine Karte aus seinen möglichen Karten wählen.
    - `makewisch(stapel, card)`: Setzt den Farb-Wunsch bei einem Buben.

- **`main.py`**: Enthält die Hauptspiellogik.
  - Funktionen:
    - `game_start()`: Initialisiert das Spiel.
    - `game()`: Führt den Hauptspielablauf aus.
    - `gen_user(player_count)`: Erstellt Spieler basierend auf der Eingabe.
    - `gen_karten()`: Generiert das Kartendeck.

### Spezialkarten

| Karte   | Effekt                                |
|---------|---------------------------------------|
| **Bube**| Spieler wählt die nächste Farbe.      |
| **Ass** | Nächster Spieler setzt aus.           |
| **7**   | Nächster Spieler zieht zwei Karten.   |

---

## Beispielablauf

1. **Spielstart**:
   - Eingabe: `Spieleranzahl: 3`
   - Spielernamen: `Spieler 1, Spieler 2, Spieler 3`

2. **Runde**:
   - **Spieler 1**: Legt eine `7`.
     - Ausgabe: `Spieler 2 muss 2 Karten ziehen.`
   - **Spieler 2**: Legt ebenfalls eine `7`.
     - Ausgabe: `Spieler 3 muss 4 Karten ziehen.`

3. **Farbwunsch**:
   - **Spieler 3**: Legt einen Buben und wünscht sich "Herz".
     - Ausgabe: `Nächste Farbe: Herz`

4. **Spielende**:
   - **Spieler 1** hat keine Karten mehr.
     - Ausgabe: `Spieler 1 hat gewonnen!`

---

## Beitrag leisten

Beitragen kannst du durch:
- Verbesserung des Codes.
- Hinzufügen neuer Features (z. B. weitere Spezialkarten).
- Bugfixes.

Erstelle dazu einen Pull Request auf GitHub.
