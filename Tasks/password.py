"""
Refactor following solution
Generate random password
"""

from random import randrange

def generate_password(alphabet, length):
    maximum = len(alphabet)
    key = ''
    for i in range(length):
        key += alphabet[randrange(0, maximum)]
    return key
