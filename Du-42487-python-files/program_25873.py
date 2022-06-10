def reverse_list(value):
    if len(value) == 0:
        return []
    return [value[-1]] + reverse_list(value[:-1])