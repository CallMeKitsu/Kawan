# Présentation :
le module **turtle.py** est la manière la plus connue et la plus utilisée de créer des représentations graphiques en python, des la 3ème en général.

**Kawan** est une simplification et une traduction du module entièrement en Français avec des paramètres expliqués et simplifiés.

Son objectif est de rendre accessible des tâches simples avec Python afin de se familiariser avec ce language à travers les fonctions, les variables, etc..

# Utilisation :
Pour utiliser Kawan, il vous suffit de télécharger le fichier [ici](https://github.com/CallMeKitsu/kawan/archive/refs/heads/main.zip "téléchargement") et de le déposer dans votre espace de travail (dans le même repertoire que votre fichier .py)

Ensuite, vous commencerez votre code par ceci :

```py
from kawan import * # importe Kawan pour l'utiliser
from turtle import * # importe turtle.py (conseillé)
```

# Fonctions Moteur :
* avancer(taille)
  >avance de la taille précisée
  
  >taille = [index des variables](https://github.com/CallMeKitsu/Kawan#variables- "index des variables")
* reculer(taille)
  >recule de la taille précisée
  
  >taille = [index des variables](https://github.com/CallMeKitsu/Kawan#variables- "index des variables")
* gauche()
  >tourne de 90° à gauche
* droite()
  >tourne de 90° à droite
* aller(x, y)
  >change la position de Kawan pour (x, y)
   
  >position = [index des variables](https://github.com/CallMeKitsu/Kawan#variables- "index des variables")

* changerX(positionX)
  >change la position X de Kawan
   
  >position = [index des variables](https://github.com/CallMeKitsu/Kawan#variables- "index des variables")
* changerY(positionY)
  >change la position Y de Kawan
   
  >position = [index des variables](https://github.com/CallMeKitsu/Kawan#variables- "index des variables")
* orienter(angle)
  >oriente Kawan selon l'angle précisé
  
  >angle = [index des variables](https://github.com/CallMeKitsu/Kawan#variables- "index des variables")
* retour()
  >change la position de Kawan pour (0, 0)
   
  >revient à la position initiale

# Fonctions Paramètres :
* dessin(booléen)
  >active ou désactive le tracé des déplacements
   
  >booléen = [index des variables](https://github.com/CallMeKitsu/Kawan#variables- "index des variables")

# Fonctions Géométriques :
* cercle(rayon)
  >trace un cercle de rayon précisé
   
  >rayon = doit être un nombre 
   
  >etendre = facultatif, arc de cercles
* point(diamètre, couleur)
  >dessine un point du diamètre et la couleur précisée
  
  >diamètre = doit être un nombre
  
  >couleur = [index des variables](https://github.com/CallMeKitsu/Kawan#variables- "index des variables")
   
 
  
# Variables :
* taille
  >la taille est le nombre d'unités que Kawan va parcourir
  
  >la taille doit être un nombre
* couleur
  >la couleur peut être : rouge, bleu, vert, cyan, rose, noir, jaune, magenta
  
  >la couleur peut être : un code [HEX](https://www.color-hex.com "sélécteur de couleur")
* booléen
  >un booléen peut être "oui" ou "non"