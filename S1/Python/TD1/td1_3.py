#######################################################
print("\n\nExercice 3\n")

def factoriel(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*factoriel(n-1)

n = int(input('Enter Int Number'))
print(factoriel(n))