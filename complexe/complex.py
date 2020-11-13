import math

class complex:

    def __init__(self,reel=None,imaginaire=None):
        self.reel = reel
        self.imaginaire = imaginaire

    def __add__(self, x):
        """Addition entre deux complexe"""
        comp = complex()
        comp.reel = self.reel + x.reel
        comp.imaginaire = self.imaginaire + x.imaginaire

        return complex(comp.reel, comp.imaginaire)

    def __sub__(self, x):
        """Soustraction entre deux complexe"""
        comp2 = complex()
        comp2.reel = self.reel - x.reel
        comp2.imaginaire = self.imaginaire - x.imaginaire
        return complex(comp2.reel, comp2.imaginaire)

    def __mul__(self, x):
        """Multiplication entre deux complexe"""
        comp3 = complex()
        comp4 = complex()
        if self.imaginaire * x.imaginaire < 0:
            a = -(self.imaginaire * x.imaginaire)
        else:
            a = self.imaginaire * x.imaginaire
        comp3.reel = (self.reel * x.reel) + a
        comp3.imaginaire = self.imaginaire * x.reel + self.reel * x.imaginaire

        return complex(comp3.reel, comp3.imaginaire)

    def mod(self):
        """Calcul du module d'un complexe"""
        comp4 = complex()
        comp4.reel = self.reel * self.reel
        comp4.imaginaire = self.imaginaire * self.imaginaire
        modulo = comp4.reel + comp4.imaginaire
        return (math.sqrt(modulo))

    def coord(self):
        """Determine les coordonéés d'un complexe"""
        cos = self.reel/self.mod()
        sin = self.imaginaire / self.mod()

        return(cos,sin)


    def point_Cercle(self,x,y):
        """Nous donnes le point sur le cercle trigonométrique par rapport a ces coordonnée, donc sont argument  """
        if(x == 1/2 and y == math.sqrt(3)/2) :
            coord = math.pi/3
        elif(x == math.sqrt(2)/2 and y == math.sqrt(2) / 2) :
            coord = math.pi / 4
        elif(x == math.sqrt(3)/2 and y == 1/2):
            coord = math.pi / 6
        elif(x == -1 / 2 and y == math.sqrt(3) / 2):
            coord = (2)*math.pi / 4
        elif(x == math.sqrt(2)/-2 and y == math.sqrt(2)/2):
            coord = (3)*math.pi / 3
        elif(x == math.sqrt(3)/-2 and y == math.sqrt(1)/2):
            coord = (5)*math.pi / 6
        elif(x == 1 / 2 and y == math.sqrt(3) / -2):
            coord = -(math.pi/3)
        elif(x == math.sqrt(2)/2 and y == math.sqrt(2)/-2):
            coord = -(math.pi / 4)
        elif(x == math.sqrt(3)/2 and y == -1/2):
            coord = -math.pi / 6
        elif(x == -1 / 2 and y == math.sqrt(3)/-2):
            coord = (-2)*math.pi / 3
        elif(x == math.sqrt(2)/-2 and y == math.sqrt(2)/-2):
            coord = (-3)*math.pi / 4
        elif(x == math.sqrt(3)/-2 and y == math.sqrt(1)/2):
            coord = (-5)*math.pi / 6
        else :
            coord = 0

        return(coord)









