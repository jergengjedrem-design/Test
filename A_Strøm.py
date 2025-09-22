import math

retning1 = float(input("Skriv inn målt strøm for retning 1: "))
retning2 = float(input("Skriv inn målt strøm for retning 2: "))

def strøm(retning1, retning2):
    total = math.sqrt(retning1**2 + retning2**2)
    return total

print("Total strømstyrke", strøm(retning1, retning2))


