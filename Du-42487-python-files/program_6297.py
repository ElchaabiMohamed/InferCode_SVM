import sys

def reverse_list(list):
    if list == []:
        return []
    elif len(list) == 1:
        newlist = []
        newlist.append(list.pop())
                  
    else:
        return reverse_list(list[1:])
