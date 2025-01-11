def check(cases, func_name):
    for args, expected in cases:
        result = globals()[func_name](*args)
        assert result == expected, f"Failed: {func_name}({args}) => {result}, expected {expected}"
    print(f"All tests passed for {func_name}!")

cases = [
    (['abc', 5], ['abc', 'abc', 'abc', 'abc', 'abc']),
    (['abc', 1], ['abc']),
    (['abc', -1], []),
    (['abc', 0], []),
    (['', 0], []),
]

check(cases, 'duplicate')
