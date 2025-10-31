#Basic iteration
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


#Using range() for counting    
for i in range(5):
    print(i)
#range(start, stop)
for i in range(2, 6):
    print(i)
#range(start, stop, step)    
for i in range(1, 10, 2):
    print(i)    


#Looping over indices of a list
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(i, fruits[i])


#Using enumerate() (Pythonic style)
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)


#Looping over characters in a string
text = "Python"
for char in text:
    print(char)


#Nested for loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


#Looping with condition (using if)
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        print(num)

#Using break inside a loop
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print(num)


#Using else with a for loop
for num in range(3):
    print(num)
else:
    print("Loop finished normally")

#List comprehension (compact for loop)
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)

