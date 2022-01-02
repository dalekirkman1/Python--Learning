<<<<<<< HEAD
"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print(type(pi))
print(pi)


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
print(i)
if i < 50:
    print("i is less than 50")
if i > 50:
    print("i is greater than 50")
   

# TODO: Write a conditional that prints the color of the picked fruit
fruit = random.choice(['orange', 'strawberry', 'banana'])
if fruit in 'orange':
    print("orange")
if fruit in 'strawberry':
    print("strawberry")
if fruit in 'banana':
    print("banana")
    
# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multiply(num1, num2 ):
    result = num1 * num2
    print(result)
 
# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =",)
multiply(12, 96) 

print("48 x 17 =",)
multiply(48, 17)

print("196523 x 87323 =",)
multiply(196523, 87323)

=======
"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print(type(pi))
print(pi)


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
print(i)
if i < 50:
    print("i is less than 50")
if i > 50:
    print("i is greater than 50")
   

# TODO: Write a conditional that prints the color of the picked fruit
fruit = random.choice(['orange', 'strawberry', 'banana'])
if fruit in 'orange':
    print("orange")
if fruit in 'strawberry':
    print("strawberry")
if fruit in 'banana':
    print("banana")
    
    
# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multiply(num1, num2 ):
    result = num1 * num2
    print(result)
    
    
# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =",)
multiply(12, 96) 

print("48 x 17 =",)
multiply(48, 17)

print("196523 x 87323 =",)
multiply(196523, 87323)

>>>>>>> bf873c5a992995129f83c8d062308c03b81bb5e2
