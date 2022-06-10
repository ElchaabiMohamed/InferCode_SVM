def get_price(age):
    if age <= 16:
            return "5"
    
    elif age > 60:
            return "7"
    
    else:
            return"10"
    
def merge_lists(l1, l2):
    l = l1[::2] + l2[::2]
    return l

def weird_case(some_str):
    diff_str = ""
    i = True
    
    for letter in some_str:
        if i:
               diff_str += letter.upper()
    
        else: 
               diff_str += letter.lower()
    
        if letter != " ":
                i = not i
    
    return diff_str

def remove_zeros(list):
    i = 0
    while i < len(list):
            if 0 in list:
                   list.remove(0)
            i = i + 1
             
    