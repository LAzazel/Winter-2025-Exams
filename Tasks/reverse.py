"""
Refactor following solution
Reverse dict, exchange keys and values
"""

def reverse(data):
    keys = list(data.keys())
    values = list(data.values())
    return dict(zip(values, keys))
