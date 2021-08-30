import turtle
import time

non = "non"
oui = "oui"
droite: int = 0
gauche: int = 180
haut: int = 90
bas: int = 270
lente = 1
rapide = 0
normale = 6


def Avancer(taille):
    turtle.forward(taille)


def Reculer(taille):
    turtle.backward(taille)


def Gauche():
    turtle.left(90)


def Droite():
    turtle.right(90)


def Tourner(sens, degre):
    if sens == gauche:
        turtle.left(degre)
    if sens == droite:
        turtle.right(degre)


def Aller(positionX, positionY):
    turtle.goto(positionX, positionY)


def ChangerX(positionX):
    turtle.setx(positionX)


def ChangerY(positionY):
    turtle.sety(positionY)


def Orienter(angle):
    print(angle)
    turtle.setheading(angle)


def Retour():
    turtle.home()


def Cercle(rayon, etendre=None):
    turtle.circle(rayon, etendre)


def Point(diametre, couleur):
    turtle.dot(diametre, couleur)


def Annuler(nombre):
    turtle.undo(nombre)


def Vitesse(valeur):
    turtle.speed(valeur)


def Dessiner(valeur):
    if valeur == oui:
        turtle.pendown()
    if valeur == non:
        turtle.penup()


def Attendre(secondes):
    time.sleep(secondes)


def Couleur(couleur):
    turtle.color(couleur)


def Pinceau(diametre):
    turtle.pensize(diametre)


def CouleurDeFond(couleur):
    turtle.bgcolor(couleur)


def Fin():
    turtle.mainloop()
