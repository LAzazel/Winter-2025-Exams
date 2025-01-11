"""
Refactor following solution
Return an array without duplicates
"""

def duplicate(value, n):
    if n:
        res = [value] * n
        return res
    return []
