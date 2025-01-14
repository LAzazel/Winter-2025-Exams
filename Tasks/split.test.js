cases = [
    [3, ['a', 'b', 'c', 'd', 'e'], [['a', 'b', 'c'], ['d', 'e']]],
    [3, [1, 2, 3, 4], [[1, 2, 3], [4]]],
    [3, ['a', 'b', 'c'], [['a', 'b', 'c'], []]],
    [3, ['a', 'b'], [['a', 'b'], []]],
    [3, [1], [[1], []]],
    [3, [], [[], []]],
]

def check(cases, func):
    for case in cases:
        index, array, expected = case
        result = func(index, array)
        assert result == expected, f"Test failed: {result} != {expected}"
    print("All tests passed!")

check(cases, split_array)
