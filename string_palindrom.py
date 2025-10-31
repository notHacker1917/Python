def isPalindrome(s):
    s = s.lower()
    rev = ""

    for ch in s:
        rev = ch + rev  

    if s == rev:
        print(s, "is a palindrome")
    else:
        print(s, "is NOT a palindrome")


word = input("Enter a word: ")
isPalindrome(word)
