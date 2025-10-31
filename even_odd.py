#even_or_odd
def checkNo(n):
    if n==0:
        print("Zero")
    elif n % 2==0:
        print("Even")
    else:
        print("Odd")
        
num=int(input("enter Num: "))
checkNo(num)
