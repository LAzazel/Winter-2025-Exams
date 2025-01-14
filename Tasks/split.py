"""
Refactor following solution
Split an array into two parts
"""

def split_array(index, array):
    begin = array[:index]
    length = len(array)
    array = array[index:length]
    return [begin, array]
