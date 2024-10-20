#######################################################
print("\n\nExercice 4\n")

def NPremier0(p):
    for i in range(2,p):
        if (p%i) == 0 :
            return False
    return p

def NPremier(p):
    for i in range(2,p):
        if (p%i) == 0 :
            return f"{p} n'est pas un nombre premier, divisible par {i}"

    return f"{p} est un nombre premier"


print(NPremier(2))