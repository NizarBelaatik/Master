#######################################################
print("\n\nExercice 5\n")

def Parfait(p):
    divstrict=[]
    for i in range(1,p):
        if p%i ==0 :
            divstrict.append(i)

    total=0
    for l in divstrict:
        total+=l
    if total == p:
        return f"{p} est un nombre parfait"
    else:
        return f"{p} n'est pas un nombre parfait"

print(Parfait(4))