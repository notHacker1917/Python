#reverse_number
def reverse(n):
    rev = 0  
    for _ in str(n):
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    print(rev)  

num = int(input("Enter num: "))
reverse(num)
