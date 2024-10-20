#######################################################
print("\n\nExercice 17\n")



def NPremier(p):
    for i in range(2,p):
        if (p%i) == 0 :
            return False
    return p


def Factoriser(n):
    if n ==1 or n==0:
        return 1
    Lfac=[]
    for i in range(2,n+1):
        if NPremier(i) and n%i==0:
            Lfac.append(i)

    #facto = '*'.join(reversed(Lfac))
    return Lfac

def mech(n):
    #if 2 in Factoriser(n) or 3 in Factoriser(n) or 5 in Factoriser(n):

    if any(x in Factoriser(n) for x in [2, 3, 5]) and len(Factoriser(n))<=3:
        print(f'le nombre {n} est mechant')
    else:
        print(f'le nombre {n} n’est pas mechant')

mech(17)
mech(30)
mech(840)