"""
Refactor following solution
Generate int array from given range
"""

def _range(from_value, to_value):
    if to_value >= from_value:
        res = [None] * (to_value - from_value + 1)
        for i in range(from_value, to_value + 1):
            res[i - from_value] = i
        return res
    return []
