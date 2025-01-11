"""
Refactor following solution
Return an array without duplicates
"""

def duplicate(value, n):
    if n:
        res = []
        for i in range(n):
            res.append(value)
        return res
    return []
