"""
Refactor following solution
Make nested array plane
"""

def const_plane(arr):
    res = []

    for i in range(len(arr)):
        value = arr[i]
        if isinstance(value, list):
            res.extend(const_plane(value))
            arr[i] = res[i - 1] if i > 0 else None
        else:
            arr[i] = res[i - 1] if i > 0 else None
            res.append(value)
    return res
