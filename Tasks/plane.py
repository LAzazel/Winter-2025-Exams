"""
Refactor following solution
Make nested array plane
"""

def const_plane(arr):
    res = []

    for i in arr:
        if isinstance(i, list):
            res.extend(const_plane(i))
        else:
            res.append(i)
    return res
