"""
Refactor following solution
Split an array into two parts
"""

def split_array(index, array):
    return [array[:index], array[index:len(array)]]
