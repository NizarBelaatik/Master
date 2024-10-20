#######################################################
print("\n\nExercice 7\n")



def U(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return U(n-1)+6*U(n-2)

print('U(n) = ',U(2))