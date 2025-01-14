cases = [
    ([[1, [[2]], [3, 4], [5], [6, [7, 8]]]], [1, 2, 3, 4, 5, 6, 7, 8]),
    ([[[[1], [[2]]], [[[3, 4], [5]], [6, [7, 8]]]]], [1, 2, 3, 4, 5, 6, 7, 8]),
    ([[[1, 2], [3, 4]]], [1, 2, 3, 4]),
    ([[1, 2, 3, 4]], [1, 2, 3, 4]),
    ([[1]], [1]),
    ([[1]], [1]),
]

for inputs, expected in cases:
    result = const_plane(*inputs)
    assert result == expected, f"Test failed for input: {inputs}, got: {result}"

print("All tests passed!")
