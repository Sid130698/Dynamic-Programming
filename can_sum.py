''' Write a function 'canSum(targetsum,members)' 
that takes in a targetSum and an Array of numbers as arguments.


The function should return a boolean indicating whether or not
it is possible to generate the targetSum using numbers from the array.

you may use an element of the array as many timesm as needed 
you may assume that all input numbers are non-negative

'''

#.........Brute Force Approach............#
#time complexity=O(n^m) space complexity =O(m)
def can_sum(targetsum,numbers):
    if targetsum == 0:return True
    if targetsum<0:
        return False
    for num in numbers:
        remainder=targetsum-num
        if can_sum(remainder,numbers):
            return True
    return False

print(can_sum(7,[5,3,4,7]))
print(can_sum(7,[2,4]))



#------------------------Dynmaic Programming and memomizing the fucntion...........................
#timeComplexity = O(n*m)    space = O(m)

def can_sum_dp(targetsum, numbers,memo={}):
    if targetsum in memo: return memo[targetsum]
    if targetsum == 0:return True
    if targetsum<0:
        return False
    for num in numbers:
        remainder=targetsum-num
        if can_sum_dp(remainder,numbers,memo):
            memo[targetsum]=True
            return True
    memo[targetsum]=False
    return False
print(can_sum_dp(300,[7,14]))
print(can_sum_dp(280,[6,14]))
