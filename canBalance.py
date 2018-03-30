# Given a non-empty array, return true if there is a place to split the array 
# so that the sum of the numbers on one side is equal to the sum of the numbers on the other side.

def canBalance(nums):
    if sum(nums) % 2 != 0:
        return False
    return True

print(canBalance([1, 1, 1, 2, 1]))
print(canBalance([2, 1, 1, 2, 1]))
print(canBalance([10, 10]))