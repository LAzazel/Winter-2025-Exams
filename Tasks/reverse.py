"""
Refactor following solution
Reverse dict, exchange keys and values
"""

def reverse(data):
    for key in list(data.keys()):
        value = data[key]
        data[value] = key
        del data[key]
    return data
