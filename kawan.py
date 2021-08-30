import turtle
import time

non = "non"
oui = "oui"
droite = 0
gauche = 180
haut = 90
bas = 270
lente = 1
rapide = 0
normale = 6
rouge = 'red'
bleu = 'blue'
vert = 'green'
cyan = 'cyan'
rose = 'rose'
noir = 'black'
jaune = 'yellow'
magenta = 'magenta'


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


def Ecrire(texte):
    turtle.write(texte, False, align="center")


def Fin():
    turtle.mainloop()
