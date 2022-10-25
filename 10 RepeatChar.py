############  10 Repeat The Characters ######

# Create a Python function that accepts a string. The function should return a string, with each character in the original string doubled. If you send the function "now" as a parameter, it should return "nnooww," and if you send "123a!", it should return "112233aa!!".

# Code Here

def RepeatChar(STR):
    result = []
    for i in range(0, len(STR)):
        result.append(STR[i]*2)
    #print(result)
    return result

STR = input("Enter a string: ")
print(RepeatChar(STR))

