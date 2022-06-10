import sys

def reverse_list(list):
    if list == []:
        return []

    else:
        return list(reverse_list(list[1:])).append(list[0])
