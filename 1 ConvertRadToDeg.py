### 1 Convert Radian To Degree ########

# Convert radians into degrees Write a function in Python that accepts one numeric parameter. This parameter will be the measure of an angle in radians. The function should convert the radians into degrees and then return that value.
# While you might find a Python library to do this for you, you should write the function yourself. One hint you get is that you'll need to use Pi in order to solve this problem. You can import the value for Pi from Python's math module.

# Code Here

from math import degrees, radians, pi
from numpy import rad2deg

# Through Simple Way
radians = float(input("Enter Radian... "))

## Through red2deg build-in function
degree = rad2deg(radians) 

## through formula
degree = radians*(180/pi)
print(degree)


#$$$$$$$$$$$$$$$$$ Through FUnction $$$$$$$$$$$$$$$$$$$$$#

def ConRadToDeg(radian):

    ## Through red2deg build-in function
    degree = rad2deg(radians) 

    ## through formula
    degree = radians*(180/pi)
    return(degree)

radians = float(input("Enter Radian... "))
ConRadToDeg(radians)
print(degree)