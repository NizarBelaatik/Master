#######################################################
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