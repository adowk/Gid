import matplotlib.pyplot as plt
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

def areal_fra_radius(r):
        return math.pi * r**2

def effekt(strom, tetthet=1000, turbin_eff=0.3, diameter=1):
        radius = diameter / 2
        areal = areal_fra_radius(radius)
        return 0.5 * turbin_eff * tetthet * areal * (strom**3)

effekter = []
totaler = []

for i in range(len(tider)):
        t = total_strom(retning1[i], retning2[i])
        totaler.append(t)
        
for i in range(len(totaler)):
        e = effekt(totaler[i])
        effekter.append(e)


plt.plot(tider, effekter)
plt.xlabel("Tid")
plt.ylabel("Effekt (W)")
plt.title("Effektproduksjon over tid")
plt.show()