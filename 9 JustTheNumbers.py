#####  9 Just The Number ###########

# Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings. The function should return a list with only the integers in the original list in the same order.

# Code Here

def Number(list1):
    global x
    result = []
    for i in list1:
        if(type(i) is int):
            result.append(i)
    x = len(result)
    return x

list1 = ['zaid', 1, 4, 'arman', 6, 3, 'python', 0, 'developer', 88]
Number(list1)
print("The length of integers in list is : ", x)

