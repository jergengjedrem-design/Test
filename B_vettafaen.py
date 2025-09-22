import math


def effekt(strøm, tetthet = 1000, turbin_effekt = 0.3, diameter = 1):
    areal = math.pi*(diameter/2)**2
    effekt = 0.5*turbin_effekt*tetthet*areal*(strøm**3)
    return effekt 

strøm = float(input("Skriv inn en strøm: "))
print(effekt(strøm))