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

tider = []
retning1 = []
retning2 = []

fil = open("tidevannsdata_csv.txt", "r")

next(fil) 

for linje in fil:
        linje = linje.strip()
        if not linje:
                continue
        tid, r1, r2 = linje.split(";")
        tider.append(float(tid))
        retning1.append(float(r1))
        retning2.append(float(r2))

fil.close()

totaler = []

for i in range(len(tider)):
        t = total_strom(retning1[i], retning2[i])
        totaler.append(t)