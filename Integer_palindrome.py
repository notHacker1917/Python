def is_palindrome_num(n):
    original = n
    rev = 0

    for _ in str(n):  
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10

    if rev == original:
        print(original, "is a palindrome")
    else:
        print(original, "is NOT a palindrome")


num = int(input("Enter a number: "))
is_palindrome_num(num)
