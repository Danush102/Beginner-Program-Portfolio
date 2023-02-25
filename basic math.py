import math

# get user input for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# perform basic math operations using built-in math functions
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
exponentiation = math.pow(num1, num2)
square_root = math.sqrt(num1)

# print the results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)
print("Square Root of", num1, ":", square_root)