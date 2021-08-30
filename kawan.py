import turtle

non = "non"
oui = "oui"
est = 0
ouest = 180
nord = 90
sud = 270



def avancer(taille):
    turtle.forward(taille)


def reculer(taille):
    turtle.backward(taille)


def gauche():
    turtle.left(90)


def droite():
    turtle.right(90)


def aller(positionX, positionY):
    turtle.goto(positionX, positionY)


def x(positionX):
    turtle.setx(positionX)


def y(positionY):
    turtle.sety(positionY)


def orienter(valeur):
    turtle.setheading(valeur)


def retour():
    turtle.home()


def cercle(rayon, etendre=None):
    turtle.circle(rayon, etendre)


def point(taille, couleur):
    turtle.dot(taille, couleur)


def annuler(nombre):
    turtle.undo(nombre)


def vitesse(valeur):
    turtle.speed(valeur)


def dessin(valeur):
    if valeur == oui:
        turtle.pendown()
    if valeur == non:
        turtle.penup()


def fin():
    turtle.mainloop()
