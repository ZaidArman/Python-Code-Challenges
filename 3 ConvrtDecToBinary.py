#### 3 Convert Decimal to Binary #########

# Convert a decimal number into binary Write a function in Python that accepts a decimal number and returns the equivalent binary number. To make this simple, the decimal number will always be less than 1,024, so the binary number returned will always be less than ten digits long.

# Code Here

def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')

# decimal value
decimal_value = int(input("Input Decimal Number for converting... "))
     
# Calling function
DecimalToBinary(decimal_value)

