import math
from typing import Tuple, Optional, Union


class Complex:
    def __init__(self, reel: Optional[Union[float, int]] = None, imaginaire: Optional[Union[float, int]] = None):
        self.reel = reel
        self.imaginaire = imaginaire
        # You could compute the modulus and argument here and set them as object attributes

    def __add__(self, x: "Complex") -> "Complex":
        """Addition entre deux complex"""
        comp = Complex()
        comp.reel = self.reel + x.reel
        comp.imaginaire = self.imaginaire + x.imaginaire

        return Complex(comp.reel, comp.imaginaire)

    def __sub__(self, x: "Complex") -> "Complex":
        """Soustraction entre deux complex"""
        comp = Complex(self.reel - x.reel, self.imaginaire - x.imaginaire)
        return comp

    def __mul__(self, x: "Complex") -> "Complex":
        """Multiplication entre deux complex"""

        # No need for ifs : (a + ib)(c + id) = (ac - bd)(ad + bc)

        # comp = Complex()
        # if self.imaginaire * x.imaginaire < 0:
        #     a = -(self.imaginaire * x.imaginaire)
        # else:
        #     a = self.imaginaire * x.imaginaire
        # comp.reel = (self.reel * x.reel) + a
        # comp.imaginaire = self.imaginaire * x.reel + self.reel * x.imaginaire

        return Complex(
            self.reel * x.reel - self.imaginaire * x.imaginaire, self.reel * x.imaginaire + self.imaginaire * x.reel
        )

    def mod(self) -> float:
        """Calcul du module d'un complex z1 = complex(1,2) z1.mod() = racine(5)"""
        comp = Complex()
        comp.reel = self.reel * self.reel
        comp.imaginaire = self.imaginaire * self.imaginaire
        modulo = comp.reel + comp.imaginaire
        return math.sqrt(modulo)

    def coord(self) -> Tuple[float, float]:
        """Determine les coordonéés d'un complex z1 = complex(1,2) z1.coord() = (1/racine(5), 2/racine(5)

        To give an example in a docstring, do that:

        Example
        -------
        >>> from complex import Complex
        >>> z = Complex(2, 2)
        >>> z.coord()
        (0.7071067811865475, 0.7071067811865475)
        """
        cos = self.reel / self.mod()
        sin = self.imaginaire / self.mod()

        return cos, sin

    @staticmethod  # This method does not use "self", so remove it and set the method as static
    def point_cercle(x: float, y: float) -> float:
        """Nous donnes le point sur le cercle trigonométrique par rapport a ces coordonnée, donc sont argument
        z1.z1.point_Cercle(1/2,math.sqrt(3)/2) == math.pi/3

        Unclear docstring : I do not understand this method in less than 30 seconds, which is the point of a docstring
        """
        if x == 1 / 2 and y == math.sqrt(3) / 2:
            coord = math.pi / 3
        elif x == math.sqrt(2) / 2 and y == math.sqrt(2) / 2:
            coord = math.pi / 4
        elif x == math.sqrt(3) / 2 and y == 1 / 2:
            coord = math.pi / 6
        elif x == -1 / 2 and y == math.sqrt(3) / 2:
            coord = 2 * math.pi / 4
        elif x == math.sqrt(2) / -2 and y == math.sqrt(2) / 2:
            coord = 3 * math.pi / 3
        elif x == math.sqrt(3) / -2 and y == math.sqrt(1) / 2:  # (**)
            coord = 5 * math.pi / 6
        elif x == 1 / 2 and y == math.sqrt(3) / -2:
            coord = -(math.pi / 3)
        elif x == math.sqrt(2) / 2 and y == math.sqrt(2) / -2:
            coord = -(math.pi / 4)
        elif x == math.sqrt(3) / 2 and y == -1 / 2:
            coord = -math.pi / 6
        elif x == -1 / 2 and y == math.sqrt(3) / -2:
            coord = (-2) * math.pi / 3
        elif x == math.sqrt(2) / -2 and y == math.sqrt(2) / -2:
            coord = (-3) * math.pi / 4
        elif x == math.sqrt(3) / -2 and y == math.sqrt(1) / 2:  # This condition is the same as (**) : why ?
            coord = (-5) * math.pi / 6
        else:
            coord = 0

        return coord
