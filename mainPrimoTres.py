#funcion
def is_prime(a):
    
    counter = 0
    for i in range(1,a+1):
        if a% i==0:
            counter = counter + 1
    if counter==2:
        a=a**0
        return a
    else:
        a=a*0
        return a
    

#codigo

pr=0
while True:
    pr=pr+1
    try:
        n=int(input("Valor a evaluar: "))
        if n < 0:
            print("numero menor que cero asi que pailas")
            break
        primo=is_prime(n)
        if primo==0:
            print(primo)
        else:
            print(primo)
    except Exception:
        print("-1")

con=0
for i in range(1,pr+1):
    
    if pr% i==0:
        con = con + 1
if con==2:
    
    print("la cantidad de veces calculadas es prima y es: ",pr)
       
else:
    print("la cantidad de veces calculadas no es prima y es: ",pr)
        
        
