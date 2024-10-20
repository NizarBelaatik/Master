
#######################################################
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





