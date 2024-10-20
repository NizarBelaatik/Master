#######################################################
print("\n\nExercice 16\n")

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
            Lfac.append(str(i))

    #facto = '*'.join(reversed(Lfac))
    return Lfac

#print(' Factoriser(30) = ',Factoriser(30))
print('Factoriser(30) = ','*'.join(reversed(Factoriser(30))))
print('Factoriser(840) = ','*'.join(reversed(Factoriser(840))))

