# Présentation :
le module **turtle.py** est la manière la plus connue et la plus utilisée de créer des représentations graphiques en python, dès la 3ème en général.

**Kawan** est une simplification et une traduction du module entièrement en Français avec des paramètres expliqués et simplifiés.

Son objectif est de rendre accessible des tâches simples avec Python afin de se familiariser avec ce language à travers les fonctions, les variables, etc..

# Utilisation :
Pour utiliser Kawan, il vous suffit de télécharger le fichier [ici](https://github.com/CallMeKitsu/kawan/archive/refs/heads/main.zip "téléchargement") et de le déposer dans votre espace de travail (dans le même repertoire que votre fichier .py)

Ensuite, vous commencerez votre code par ceci :

```py
from kawan import * # importe Kawan pour l'utiliser
from turtle import * # importe turtle.py (conseillé)
```

Conseil : pour laisser tourner la fenêtre d'affichage du rendu graphique, il est recommandé de placer la fonction :
```py
Fin() # égal à : turtle.mainloop()
```
À la fin de votre code, après toutes les autres fonctions de Kawan !

# Fonctions Moteur :
* Avancer(taille)
  >avance de la taille précisée
  
  >taille = [index des variables](https://github.com/CallMeKitsu/Kawan#variables- "index des variables")
* Reculer(taille)
  >recule de la taille précisée
  
  >taille = [index des variables](https://github.com/CallMeKitsu/Kawan#variables- "index des variables")
* Gauche()
  >tourne de 90° à gauche
* Droite()
  >tourne de 90° à droite
* Tourner(direction, degré)
  >tourner dans une direction à un certain degré
  
  >direction = peut être gauche / droite / haut / bas
  
  >degré = doit être un nombre, sans °
* Aller(x, y)
  >change la position de Kawan pour (x, y)
   
  >position = [index des variables](https://github.com/CallMeKitsu/Kawan#variables- "index des variables")

* ChangerX(positionX)
  >change la position X de Kawan
   
  >position = [index des variables](https://github.com/CallMeKitsu/Kawan#variables- "index des variables")
* ChangerY(positionY)
  >change la position Y de Kawan
   
  >position = [index des variables](https://github.com/CallMeKitsu/Kawan#variables- "index des variables")
* Orienter(angle)
  >oriente Kawan selon l'angle précisé
  
  >angle = [index des variables](https://github.com/CallMeKitsu/Kawan#variables- "index des variables")
* Retour()
  >change la position de Kawan pour (0, 0)
   
  >revient à la position initiale

# Fonctions Paramètres :
* Dessiner(booléen)
  >active ou désactive le tracé des déplacements
   
  >booléen = [index des variables](https://github.com/CallMeKitsu/Kawan#variables- "index des variables")
* Couleur(couleur)
  >change la couleur du pinceau
  
  >couleur = [index des variables](https://github.com/CallMeKitsu/Kawan#variables- "index des variables")

* CouleurDeFond(couleur)
  >change la couleur du fond
  
  >couleur = [index des variables](https://github.com/CallMeKitsu/Kawan#variables- "index des variables")
* Pinceau(diametre)
  >change le diamètre du pinceau
   
  >diametre = doit être un nombre 
* Vitesse(vitesse)
  >change la vitesse à laquelle les actions sont effectuées

  >vitesse = [index des variables](https://github.com/CallMeKitsu/Kawan#variables- "index des variables")
   
# Fonctions Géométriques :
* Cercle(rayon)
  >trace un cercle de rayon précisé
   
  >rayon = doit être un nombre 
   
  >etendre = facultatif, arc de cercles
* Point(diamètre, couleur)
  >dessine un point du diamètre et la couleur précisée
  
  >diamètre = doit être un nombre
  
  >couleur = [index des variables](https://github.com/CallMeKitsu/Kawan#variables- "index des variables")

# Fonctions Diverses :
* Annuler(nombre)
  >annule un nombre d'actions effectuées
  
  >nombre = doit être un nombre, inférieur au nombre d'actions 
* Attendre(secondes)
  >attends le nombre de secondes avant d'effectuer la suite

  >secondes = doit être un nombre
* Fin()
  >termine le programme et le laisse tourner (recommandé)
# Variables :
* taille
  >la taille est le nombre d'unités que Kawan va parcourir
  
  >la taille doit être un nombre
* couleur
  >la couleur peut être : rouge, bleu, vert, cyan, rose, noir, jaune, magenta
  
  >la couleur peut être : un code [HEX](https://www.color-hex.com "sélécteur de couleur")
* booléen
  >un booléen peut être "oui" ou "non"
* angle
  >l'angle peut être : haut, bas, gauche, droite
  
  >l'angle peut être : un nombre, sans °
* vitesse
  >la vitesse peut être : rapide, lente, normale

  >la vitesse peut être : un nombre, de 0 à 10
  
# Avancement :
- [x] forward()
- [x] backward()
- [X] right()
- [X] left() 
- [x] goto() 
- [x] setx()
- [x] sety()
- [x] setheading()
- [x] home()
- [x] circle()
- [x] dot()
- [ ] stamp()
- [ ] clearstamp()
- [ ] clearstamps()
- [x] undo()
- [x] speed()
- [x] pendown()
- [x] penup()
- [X] pensize()
- [ ] position()
- [X] color()
- [X] bgcolor()