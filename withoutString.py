# Given two strings, base and remove, return a version of the base string 
# where all instances of the remove string have been removed (not case sensitive). 
# You may assume that the remove string is length 1 or more. Remove only non-overlapping instances, 
# so with "xxx" removing "xx" leaves "x".

import string

def withoutString(base, remove):
    idx = 0
    length = len(base)
    rlen = len(remove)
    while string.find(base, remove) != -1:
        idx = string.find(base, remove)
        base = base[0:idx] + base[idx+rlen:]
    return base

print(withoutString("Hello there", "llo"))
print(withoutString("Hello there", "e"))
print(withoutString("Hello there", "x"))