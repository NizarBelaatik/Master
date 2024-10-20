#######################################################
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