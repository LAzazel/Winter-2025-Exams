// Refactor following solution
// Return an array without duplicates

def duplicate(value, N):
    if N <= 0:
        return []
    else:
        res = []
        for i in range(N):
            res.append(value)
        return res
