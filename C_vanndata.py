import math
import matplotlib.pyplot as plt

tid = []
retning1 = []
retning2 = []
total = []
total_effekt = []

def effekt(strøm, tetthet = 1000, turbin_effekt = 0.3, diameter = 1):
    areal = math.pi*(diameter/2)**2
    effekt = 0.5*turbin_effekt*tetthet*areal*(strøm**3)
    return effekt


with open("Oving_5/tidevannsdata_csv.txt", "r", encoding = "UTF8") as vann:
    next(vann)
    for linje in vann:
        deler = linje.split(";")
        t = float(deler[0])
        r1 = float(deler[1])
        r2 = float(deler[2])

        tid.append(t)
        retning1.append(r1)
        retning2.append(r2)

print("tid:", tid)
print("Retning 1: ", retning1)
print("Retning 2: ", retning2)


for i in range(len(tid)):
    verdi = math.sqrt(retning1[i]**2 + retning2[i]**2)
    total.append(verdi)

print("total:", total)

plt.plot(tid, total)
plt.show()

for i in range(len(total)):
    res = effekt(total[i])

    total_effekt.append(res)

print("Total effekt :", total_effekt)
    
plt.plot(tid, total_effekt)
plt.show()

antall = 0
samlet = 0

for linje in total_effekt:
    antall += 1
    samlet += i
    try:
        gjennomsnitt = samlet/antall
    except:
        ZeroDivisionError

print("Samlet verdi av listen er:",(samlet))
print("Antall linjer i lister er:", (antall))

print("Gjennomsnitt strøm er:", gjennomsnitt)
print(round(effekt(gjennomsnitt)))




        

