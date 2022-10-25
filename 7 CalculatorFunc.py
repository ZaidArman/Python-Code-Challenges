 ##### 7. Create a calculator function #####

# Write a Python function that accepts three parameters. The first parameter is an integer. The second is one of the following mathematical operators: +, -, /, or . The third parameter will also be an integer.

# The function should perform a calculation and return the results. For example, if the function is passed 6 and 4, it should return 24.


# Code Here

def Calculator(a, op, b):
    
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '/':
        result = a / b
    elif op == '*':
        result = a * b
    else:
        print("Invalid Operator!")
    
    return result

result = 0
Number1 = int(input("Enter number for a: "))
operator = input("Enter an operator:( +, -, /, *)..... ")
Number2 = int(input("Enter number for b: "))

print(Calculator(Number1, operator, Number2))