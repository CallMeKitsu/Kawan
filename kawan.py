import turtle
import time

turtle.shape("turtle")  # apparence par défaut de Kawan
turtle.color('green')  # apparence par défaut de Kawan

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
    for i in range(nombre):
        turtle.undo()


def Vitesse(valeur):
    turtle.speed(valeur)


def Dessiner(booleen):
    if booleen == oui:
        turtle.pendown()
    if booleen == non:
        turtle.penup()


def Attendre(secondes):
    time.sleep(secondes)


def Couleur(couleur):
    turtle.color(couleur)


def Pinceau(diametre):
    turtle.pensize(diametre)


def Ecrire(texte):
    turtle.write(texte, False, align="center")


def Visible(booleen):
    if booleen == non:
        turtle.hideturtle()
    if booleen == oui:
        turtle.showturtle()


def Triangle(taille):
    for i in range(3):
        turtle.forward(taille)
        turtle.left(120)


def Carre(taille):
    for i in range(4):
        turtle.forward(taille)
        turtle.left(90)


def Fin():
    turtle.mainloop()
