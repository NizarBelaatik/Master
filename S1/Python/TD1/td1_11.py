#######################################################
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