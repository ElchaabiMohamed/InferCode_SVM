def swap_keys_and_values(swap_me):
    return {swap_me[key] : key for key in list(swap_me.keys())}
