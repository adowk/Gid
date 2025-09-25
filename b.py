import math
import os

def clear():
        if os.name == "nt":
                os.system("cls")
        else:
                os.system("clear")

clear()

def areal_fra_radius(r):
        return math.pi * r**2

def effekt(strom, tetthet=1000, turbin_eff=0.3, diameter=1):
        radius = diameter / 2
        areal = areal_fra_radius(radius)
        return 0.5 * turbin_eff * tetthet * areal * (strom**3)
