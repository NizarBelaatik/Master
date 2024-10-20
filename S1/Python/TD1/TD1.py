
##############################################################################################################
##############################################################################################################
print("Exercice 1\n")

while True:
    a = int(input('Enter Positive Num :  '))
    if a>0:
        break
bina=''
while( a>0):
    p=a%2
    a=a//2
    bina=str(p)+bina

print(bina)





##############################################################################################################
##############################################################################################################
print("\n\nExercice 2\n")


#U(0)=N
def Syracuse(n):
    if n== 0:
        return N
    elif(Syracuse(n-1)) % 2 ==0:
        return Syracuse(n-1)/2
    else:
        return (3*Syracuse(n-1))+1

#
def syracuse(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return syracuse(n // 2)
    else:
        return syracuse(3 * n + 1)

def indice(N):
    count=0
    while N!=1:
        count +=1
        if N%2 ==0:
            N=N//2
        else:
            N=3*N+1
    return count
N=4
print('Syracuse == ',Syracuse(5))
print('indice == ',indice(N))



##############################################################################################################
##############################################################################################################
print("\n\nExercice 3\n")

def factoriel(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*factoriel(n-1)

n = int(input('Enter Int Number'))
print(factoriel(n))


##############################################################################################################
##############################################################################################################
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


##############################################################################################################
##############################################################################################################
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


##############################################################################################################
##############################################################################################################
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




##############################################################################################################
##############################################################################################################
print("\n\nExercice 7\n")

def U(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return U(n-1)+6*U(n-2)

print('U(n) = ',U(2))





##############################################################################################################
##############################################################################################################
print("\n\nExercice 8\n")


def Power(n,p):
    if n<0 or p<0:
        return False
    return n**p

print("n^p = ",Power(2,4))#int(2),int(4)



##############################################################################################################
##############################################################################################################
print("\n\nExercice 9\n")

N = 23#int(input("Enter Int Number"))

def nbrChiff(N):
    nbrc= len(str(N))
    print(nbrc)


nbrChiff(N)




##############################################################################################################
##############################################################################################################
print("\n\nExercice 11\n")

def factoriel(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*factoriel(n-1)

def expo(x,n):
    ex=0
    for i in range(n+1):
        ex+=(x**i)/factoriel(n)
    return ex

x = 1
n = 10
print(f"e^{x} jusqu'à l'ordre {n} est : {expo(x,n)}")


##############################################################################################################
##############################################################################################################
print("\n\nExercice 13\n")


def somme(n):
    a=8
    b=12
    c=6
    d=1
    for _ in range(n-1):
        a+=a
        b+=b
        c+=c
        d+=d
        print('a')
    return a,b,c,d

A,B,C,D = somme(3)
print(f"{A}k^3 + {B}k^2 + {C}K + {D}")



##############################################################################################################
##############################################################################################################
print("\n\nExercice 14\n")


def PGDS(n):
    div=[]
    for i in range(2,n):
        if n%i ==0 :
            div.append(i)

    if not div:
        return -1
    else:
        return div[-1]

print(' Plus Gran Div Strict = ',PGDS(20))





##############################################################################################################
##############################################################################################################
print("\n\nExercice 15\n")

def NPremier(p):
    for i in range(2,p):
        if (p%i) == 0 :
            return False
    return p


def PGDP(n):
    if n==1:
        return 1

    div=[]
    for i in range(1,n+1):
        if n%i ==0 :
            div.append(i)
    div2 = [1]
    for d in div:
        for j in range(1,d+1):
            if NPremier(j) and d%j==0:
                if j not in div2:
                    div2.append(j)


    return div2[-1]

print(' Plus Gran Div Prem = ',PGDP(17))





##############################################################################################################
##############################################################################################################
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





##############################################################################################################
##############################################################################################################
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



