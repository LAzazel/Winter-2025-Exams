cases = [
    ((10, 15), [10, 11, 12, 13, 14, 15]),
    ((-2, 2), [-2, -1, 0, 1, 2]),
    ((2, -2), []),
    ((2, 2), [2]),
    ((0, 0), [0]),
]

for inputs, expected in cases:
    result = _range(*inputs)
    assert result == expected, f"Test failed for input: {inputs}, got: {result}"

print("All tests passed!")
