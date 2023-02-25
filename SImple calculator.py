print("""
To find the sum of two numbers click '+'\n
To find the difference of two numbers click '-'\n
To find the product of two numbers click '*'\n
To divide two numbers click '/'\n
To find the reminder when we divide two numbers click '%'\n
For floor division for two numbers click '//'\n
To find the exponent of two numbers (number one to the power number 2) click '^'.
""")


operator=input("Enter an operator (+ - / * % ^ //) \t")

#addition
if operator == "+":
    num1=float(input("enter 1st number \t"))
    num2=float(input("enter second number \t"))
    result=round(num1+num2,3)
    print(f"the sum is:\t {result}")

#subraction
elif operator == "-":
    num1=float(input("enter 1st number \t"))
    num2=float(input("enter second number \t"))
    result=round(num1-num2,3)
    print(f"the difference is:\t {result}")

#multiplication
elif operator == "*":
    num1=float(input("enter 1st number \t"))
    num2=float(input("enter second number \t"))
    result=round(num1*num2,3)
    print(f"the product is:\t {result}")

#division
elif operator == "/":
    num1=float(input("enter 1st number \t"))
    num2=float(input("enter second number \t"))
    if num2 == 0:
        print("division is invalid")
    else:
        result=round(num1/num2,3)
        print(f"the division is:\t {result}")

#floor division
elif operator == "//":
    num1=float(input("enter 1st number \t"))
    num2=float(input("enter second number \t"))
    result=num1//num2
    print(f"the floor division is:\t {result}")

#remainder or modulus
elif operator == "%":
    num1=float(input("enter 1st number \t"))
    num2=float(input("enter second number \t"))
    result=num1-num2
    print(f"the reminder is:\t {result}")

#exponent
elif operator == "^":
    num1=float(input("enter 1st number \t"))
    num2=float(input("enter second number \t"))
    result=num1**num2
    print(f"the exponent is:\t {result}")

else:
    print(f"You have entered an invalid operator{operator}")


