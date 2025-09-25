Oppgave a:
Repetisjon: Skriv en funksjon som beregner og returnerer total strøm basert på målt strøm i to retninger. Formelen for dette er den samme som for euklidsk distanse, 𝑡𝑜𝑡𝑎𝑙 = √𝑟𝑒𝑡𝑛𝑖𝑛𝑔1 2 + 𝑟𝑒𝑡𝑛𝑖𝑛𝑔2 2

``` python
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


``` 


Oppgave b:
Importer eller kopier inn funksjonen for å regne ut effekt (energiproduksjon) fra vannstrøm fra øving 3 oppgave h.
``` python
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



``` 


Oppgave c:
Åpne og les inn fila «tidevannsdata_csv.txt». For hver linje, splitt linja på semikolon for å få tidspunkt og hastighet i de to retningene. Konverter tidspunkt og de to hastighetene fra strenger til flyttall og legg dem i hver sine lister (ei liste for tidspunkt, ei liste for strøm i retning 1, og ei liste for strøm i retning 2)
``` python
import os

def clear():
        if os.name == "nt":
                os.system("cls")
        else:
                os.system("clear")

clear()

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


``` 


Oppgave d:
Bruk funksjonen i oppgave a for å regne ut total vannstrøm for alle verdiene i listene og legg resultatet i ei ny liste eller numpy array.
Hint: Du kan konvertere listene over vannstrøm for de to retningene til numpy arrayer. Deretter kan du kalle funksjonen med hele arrayene for å få en ny array med resultatet siden numpy arrayer støtter matematiske operasjoner.
``` python
totaler = []

for i in range(len(tider)):
		t = total_strom(retning1[i], retning2[i])
		totaler.append(t)
		


``` 


Oppgave e:
Plott en kurve med tid på x-aksen og total vannstrøm på y-aksen med matplotlib
``` python
import matplotlib.pyplot as plt

plt.plot(tider, totaler)
plt.xlabel("Tid")
plt.ylabel("Total vannstrøm")
plt.title("Total vannstrøm over tid")
plt.show()


``` 


Oppgave f:
Bruk formelen fra øving 3 oppgave h til å regne ut effekt produsert for hvert tidspunkt basert på total vannstrøm. Lag ei liste eller numpy array med effekt på samme vis som for vannstrøm
``` python

effekter = []

for i in range(len(totaler)):
        e = effekt(totaler[i])
        effekter.append(e)

``` 

Oppgave g:
Plott en kurve med tid på x-aksen og effekt generert på y-aksen med matplotlib
``` python
plt.plot(tider, effekter)
plt.xlabel("Tid")
plt.ylabel("Effekt (W)")
plt.title("Effektproduksjon over tid")
plt.show()


``` 


Oppgave h:
Regn ut og skriv ut gjennomsnittlig vannstrøm
``` python
gj_snitt_strom = sum(totaler) / len(totaler)
print("Gjennomsnittlig vannstrøm:", gj_snitt_strom)


``` 



Oppgave i:
Regn ut og skriv ut hvor mye effekt du får basert på denne snittstrømmen
``` python
effekt_fra_snitt = effekt(gj_snitt_strom)
print("Effekt basert på snittstrøm:", effekt_fra_snitt)

``` 



Oppgave j:
Regn ut gjennomsnittlig effekt basert på lista fra oppgave f). Skriv ut gjennomsnittlig effekt
``` python
gj_snitt_effekt = sum(effekter) / len(effekter)
print("Gjennomsnittlig effekt:", gj_snitt_effekt)

``` 

