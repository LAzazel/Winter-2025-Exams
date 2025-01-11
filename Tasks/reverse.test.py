def check(cases, func):
    for inputs, expected in cases:
        result = func(*inputs)
        assert result == expected, f"Test failed: {inputs} -> {result}, expected: {expected}"
    print("All tests passed!")

cases = [
    ([{'a': 'uno', 'b': 'due', 'c': 'tre'}], {'uno': 'a', 'due': 'b', 'tre': 'c'}),
    ([{'a': 1, 'b': 2, 'c': 3}], {1: 'a', 2: 'b', 3: 'c'}),
    ([{'a': True, 'b': False}], {True: 'a', False: 'b'}),
    ([{'a': 'uno', 'b': 2, 'c': False}], {'uno': 'a', 2: 'b', False: 'c'}),
]

check(cases, reverse)
