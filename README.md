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

# Documentation :
fonctions moteur :
* avancer(taille)
  >avance de la taille précisée
  
  >taille = doit être un nombre
* reculer(taille)
  >recule de la taille précisée
  
  >taille = doit être un nombre
* gauche()
  >tourne de 90° à gauche
* droite()
  >tourne de 90° à droite
* aller(x, y)
  >change la position de Kawan pour (x, y)
* changerX(positionX)
  >change la position X de Kawan
* changerY(positionY)
  >change la position Y de Kawan
* orienter(angle)
  >oriente Kawan selon l'angle précisé
  
  >oriente Kawan à l'ouest / est / nord / sud 
* retour()
  >change la position de Kawan pour (0, 0)
   
  >revient à la position initiale 