#funcion
def is_prime(a):
    
    counter = 0
    for i in range(1,a+1):
        if a% i==0:
            counter = counter + 1
    if counter==2:
        print ("The number is prime")
    else:
        print ("The number is not prime")

#codigo


n=int(input("ingrese un numero a estudio: "))
is_prime(n)
