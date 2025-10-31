#Factorial 
def factorial(n):
    if n==0:
        print(1)
    multi=1    
    for i in range(n):
        i=i+1
        multi = multi * i
    print(multi)

n=int(input("Enter Num: "))
factorial(n)
