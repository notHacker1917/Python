#3726. Remove Zeros in Decimal Representation
def removeZeros(n):
    num_str = str(n)
    result_str = ""    
    for digit in num_str:  
        if digit != '0':
            result_str = result_str + digit
    return int(result_str)

n=int(input("Enter No.: "))
removeZeros(n)        
