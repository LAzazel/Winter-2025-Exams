"""
Refactor following solution
Generate int array from given range
"""

def _range(from_value, to_value):
    if to_value >= from_value:
        res = [i for i in range(from_value, to_value+1)]
        return res
    return []
