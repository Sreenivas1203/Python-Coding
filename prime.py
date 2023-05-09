def primecheck(num):
    b=1
    for i in range (2,num):
        if num % i == 0:
            b=0
    if b==0 or num==1:
        print("not a prime number")
    else:
        print("prime number")
a=int(input("Enter a number:"))
primecheck(num=a)
