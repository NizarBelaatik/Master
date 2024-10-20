#######################################################
print("\n\nExercice 6\n")


import math

def carreParfait(p):
    squareRoot = p ** (1 / 2)
    if int(squareRoot)**2 ==p:
        return f"{p} est un nombre carre parfait"
    else:
        return f"{p} n'est pas un nombre carre parfait"


# printing the square root of a number
print(carreParfait(6))