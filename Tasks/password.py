"""
Refactor following solution
Generate random password
"""

from random import choices


def generate_password(alphabet, length):
    return ''.join(choices(alphabet, k=length))
