


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


while True:
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
