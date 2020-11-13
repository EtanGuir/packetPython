import math

import pytest


from complexe.complex import complex

z1 = complex(1, -3)
z2 = complex(2, 5)

def test_instantiate():
    assert z1.reel == 1
    assert z1.imaginaire == -3

def test_addition():
    assert (z1 + z2).reel == 3
    assert (z1 + z2).imaginaire == 2

def test_soustraction():
    assert (z1 - z2).reel == -1
    assert (z1 - z2).imaginaire == -8


def test_multiplication() :
    assert (z1 * z2).reel == 17
    assert (z1 * z2).imaginaire == -1


def test_modulus():
    assert z2.mod() == 5.385164807134504


def test_coord() :
    assert z1.coord() == ( 0.31622776601683794,-0.9486832980505138)


def test_pointCoord() :
    assert z1.point_Cercle(1/2,math.sqrt(3)/2) == math.pi/3

