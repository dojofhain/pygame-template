import pygame
from helper.game import Game
from helper.image import Image

# Breite und Höhe unseres Fensters werden als Konstanten definiert
BREITE = 800
HOEHE = 600

# Farben, die wir öfters verwenden möchten, definieren wir als Konstanten
WEISS = (255, 255, 255)
GRUEN = (0, 255, 0)

# andere Konstanten
KREIS_RADIUS = 20
SCHRITT_WEITE = 5

class MeinSpiel(Game):

    # Die ist der Anfangsspunkt (Contructor) für unser Spiel. Er wird einmal beim Erzeugen aufgerufen.
    # Hier können wir zum Beispiel Variablen anlegen.
    def __init__(self):
        super().__init__(width=BREITE, height=HOEHE)

        # Wir laden das Bild eines Smileys aus einer Datei und setzen ihn in die Mitte des Bildschirms
        self.smiley = Image('smiley.png')
        self.smiley.x = (BREITE - self.smiley.width()) / 2
        self.smiley.y = (HOEHE - self.smiley.height()) / 2

        # Wir legen die Position des Rechtecks fest
        self.rechteck = pygame.Rect((BREITE - 100) / 2, HOEHE - 40, 100, 20)

        # Wir legen die Position des Kreises fest
        self.kreis_x = 0
        self.kreis_y = HOEHE / 2

    # Diese Funktion wird für jeden Schritt in unserem Spiel aufgefrufen.
    # Hier können wir zum Beispiel:
    #   - Zeichenfunktionen aufrufen
    #   - Variablen verändern
    def update(self):
        # zeichne den Smiley
        self.draw_image(image=self.smiley)

        # zeichne das Rechteck
        self.draw_rect(rect=self.rechteck, color=WEISS)

        # bewege den Kreis
        self.kreis_x += SCHRITT_WEITE
        if self.kreis_x > BREITE + KREIS_RADIUS:
            self.kreis_x = -KREIS_RADIUS

        # zeichne den Kreis
        self.draw_circle(position=(self.kreis_x, self.kreis_y), color=WEISS, radius=KREIS_RADIUS)

        # zeichne einen Text
        self.draw_text("Hallo Welt!", position=(50, 50), color=GRUEN, size=32)

    # Diese Funktion wird aufgerufen, wenn eine Taste gedrückt wurde.
    def keys_pressed(self, keys):
        # Wenn die 'Pfeil nach links'-Taste gedückt wird, bewegen wir das Rechteck nach links
        if keys[pygame.K_LEFT]:
            self.rechteck.x -= SCHRITT_WEITE
        # Wenn die 'Pfeil nach rechts'-Taste gedückt wird, bewegen wir das Rechteck nach rechts
        elif keys[pygame.K_RIGHT]:
            self.rechteck.x += SCHRITT_WEITE


meinSpiel = MeinSpiel()  # das Spiel wird erzeugt
meinSpiel.start()  # das Spiel wird gestartet
