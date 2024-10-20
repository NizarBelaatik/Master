#######################################################
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