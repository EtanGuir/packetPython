# packetPython

###### General remark : write in English

Ce dépot est un paquet python implémentant la notion de nombre complexe avec des fonctions qui différente tests 

###### This part is useless, everyone knows how a package is made ^^

Il contient un dossier avec un un dossier complexe, ce dossier contient un fichier complex qui contient une class
 complexe qui elle même contient les fonctions. Ce packet contient aussi un dossier test qui contient lui même un fichier test_complex qui test toute les fonctions. 

###### Use the folowwing synthax to give examples :

```python
from complex import Complex
z1 = Complex(1, 2)
z2 = Complex(3, 4)
z3 = z1 + z2
z4 = z1 - z2
z5 = z1 * z2
...
```

Utilisation de la fonction add (addition) : C'est une magique méthode elle permet d'aditionner deux complexe, en calculant leur partie reel ensemble et leur partie imaginaire ensemble. 

Utilisation de la fonction sub (soustraction) : C'est une magique méthode elle permet de soustraire deux complexe, en calculant leur partie reel ensemble et leur partie imaginaire ensemble. 

Utilisation de la fonction mult (multiplication) : C'est une magique méthode elle permet de multiplier deux complexe, en faisant la distributivité. 

Utilisation de  la fonction mod : Qui permet de trouver le module du d'un complexe, pour l'utiliser il faut créer un complexe avec des coordonnées, et ensuite et appeler ce complex.mod() ce qui nous donnera son module

Utilisation de la fonction coord : Elle permet de nous donner les coordonnées d'un complexe, pour l'utiliser il faut faire leComplex
.coord()

Utilisation de la fonction Elle permet de nous donner l'argument d'un nombre complexe. Pour l'utiliser il faut faire notre complexe pour lequel on veut son argument qui appel la fonction coord avec en parametre les coord cos et sin donc : monComplexe.coord(x, y) git
