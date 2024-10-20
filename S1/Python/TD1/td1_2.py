#######################################################
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
