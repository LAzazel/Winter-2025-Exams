"""
Refactor following solution
Generate random password
"""

import random

def generate_password(alphabet, length):
    maximum = len(alphabet)
    key = ''
    for i in range(length):
        index = random.randrange(0, maximum)
        key += alphabet[index]
    return key
