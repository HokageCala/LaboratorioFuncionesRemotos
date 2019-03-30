def perfect_number(n):
    a=0
    for i in range(1,n):
        if(n%i==0):
            a+=i
    if (a==n):
        print("this is a perfect number")
    else:
        print("this is not a perfet number")

n=int(input("enter a number, plis: "))
perfect_number(n)
