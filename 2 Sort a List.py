############  2 Sort a List ##############

#  Create a function in Python that accepts two parameters. The first will be a list of numbers. The second parameter will be a string that can be one of the following values: asc, desc, and none.
#  If the second parameter is "asc," then the function should return a list with the numbers in ascending order. If it's "desc," then the list should be in descending order, and if it's "none," it should return the original list unaltered.


# Code Here

from typing import Any

def sort_list(operation_list: list, choice_list: list) -> Any:
    choice = input("choice only string not number --> asc, desc, none ,exit :")
    while len(choice_list) == 3:
        if choice.lower() == 'asc':
            return sorted(operation_list, reverse=False)
        elif choice.lower() == 'desc':
            return sorted(operation_list, reverse=True)
        else:
            return operation_list

list_numbers: list = [1, 3, 2, 4, 5]
compare_list: list = ['asc', 'desc', None]
ans_sorted = sort_list(list_numbers, compare_list)
print(ans_sorted)

