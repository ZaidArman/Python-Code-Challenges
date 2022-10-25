####  5  Hide Credit Card Number ######

# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "4444444444444444", then it should return "4444".


# Code Here 

###### By Using Regex ############
import re
def mask_cc_number(cc_string, digits_to_keep=4, mask_char='*'):
   cc_string_total = sum(map(str.isdigit, cc_string))

   if digits_to_keep >= cc_string_total:
       print("Not enough numbers. Add 10 or more numbers to the credit card number.")

   digits_to_mask = cc_string_total - digits_to_keep
   masked_cc_string = re.sub('\d', mask_char, cc_string, digits_to_mask)

   return masked_cc_string
print(mask_cc_number(" 7788 9911 2233 4455 "))





######## Using def Function Simple way #####################

def CreditCard(CardNo):
    str = ''
    for char in CardNo[:-4]:
        str += '*'
    str += CardNo[-4:]
    return str

CreditCardNo = input("Enter Credit card Number... ")
print(CreditCard(str))



