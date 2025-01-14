chars = 'abc123'

cases = [
    (['abc123', 7], lambda s: len(s) == 7),
    (['abc123', 7], lambda s: all(char in chars for char in s)),
]

for inputs, test in cases:
    result = generate_password(*inputs)
    assert test(result), f"Test failed for input: {inputs}, got: {result}"

print("All tests passed!")
