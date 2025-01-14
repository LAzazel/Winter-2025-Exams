"""
Refactor following solution
Generate random password
"""

from random import choices


def generate_password(alphabet, length):
    passw = choices(alphabet, k=length)
    return ''.join(passw)
