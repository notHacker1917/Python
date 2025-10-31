#sum_of_digit
def sumDigit(n):
    sum=0
    for _ in str(n):
        mod=n%10
        sum=sum+mod
        n= n//10
    print(sum)

num=int(input("Enter num: "))
sumDigit(num)
