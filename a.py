import os
import math

def clear():
        if os.name == "nt":
                os.system("cls")
        else:
                os.system("clear")

clear()


def total_strom(r1, r2):
        return math.sqrt(r1**2 + r2**2)
