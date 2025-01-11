"""
Refactor following solution
Reverse dict, exchange keys and values
"""

def reverse(data):
    keys = list(data.keys())

    for key in keys:
        value = data[key]
        data[value] = key
        del data[key]
    return data
