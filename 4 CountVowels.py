#####  4  Count the Vowels ##########

#  Create a function in Python that accepts a single word and returns the number of vowels in that word. In this function, only a, e, i, o, and u will be counted as vowels — not y.


# Code Here 


##### Using def Function
def countvowels(string):
    num_vowels = 0
    for char in string:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels

string = input("input a String for counting vowels...")
countvowels(string)
print(countvowels(string))


#### Without def function ########
string= input("Enter string:")
vowels=0
def Vowel()
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)