############  6 Count X's and O's ############

# Create a Python function that accepts a string. This function should count the number of Xs and the number of Os in the string. It should then return a boolean value of either True or False.

# If the count of Xs and Os are equal, then the function should return True. If the count isn't the same, it should return False. If there are no Xs or Os in the string, it should also return True because 0 equals 0. The string can contain any type and number of characters.

# Code Here

def XsOsEqual(STR):
    x_count = 0
    o_count = 0
    for i in STR:
        if i == 'x' or i == 'X':
            x_count += 1
        elif i == 'o' or i == 'O':
            o_count += 1
            
    if x_count == o_count:
        bool = True
    else:
        bool = False
    return bool

STR = input("Enter a string of Xs and Os: ")
print(XsOsEqual(STR))

