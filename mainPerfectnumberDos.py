def perfect_number(n):
    a=0
    for i in range(1,n):
        if(n%i==0):
            a+=i
    if (a==n):
        print("this is a perfect number")
    else:
        print("this is not a perfet number")
    if a<=(n-3) and a>=(n+3):
        print("it's not  an almost perfect number")
    else:
        print("it's an almost perfect number") 

n=int(input("enter a number, plis: "))
perfect_number(n)
 
