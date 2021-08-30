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

# Documentation :
La documentation et toutes les informations sur Kawan sont disponibles [ici](https://github.com/CallMeKitsu/Kawan/wiki "documentation") !

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
- [ ] ~~stamp()~~
- [ ] ~~clearstamp()~~
- [ ] ~~clearstamps()~~
- [x] undo()
- [x] speed()
- [x] pendown()
- [x] penup()
- [X] pensize()
- [ ] ~~position()~~
- [X] color()
- [X] bgcolor()