"""
Refactor following solution
Generate int array from given range
"""

def _range(from_value, to_value):
    if to_value >= from_value:
        return [i for i in range(from_value, to_value+1)]
    return []
