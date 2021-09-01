'''
similar to can_sum just return the combination of elements that add up to exactly the target sum
'''


#........................Brute Force Approach.................
#time complexity= O(n^m *m) space =O(m)

def how_sum(targetsum,numbers):
    if targetsum == 0:return []
    if targetsum<0:
        return None
    for num in numbers:
        remainder=targetsum-num
        remainder_result=how_sum(remainder,numbers)
        if remainder_result is not None:
            remainder_result.append(num)
            return remainder_result
                     
    return None

print(how_sum(7,[5,3,4,7]))
print(how_sum(7,[2,4]))


#------------------------Dynmaic Programming and memomizing the fucntion...........................
#timeComplexity = O(n*m^2)    space = O(m^2)

def how_sum_dp(targetsum, numbers,memo={}):
    if targetsum in memo: return memo[targetsum]
    if targetsum == 0:return []
    if targetsum<0:
        return None
    for num in numbers:
        remainder=targetsum-num
        res=how_sum_dp(remainder,numbers,memo)
        if res is not None:
            res.append(num)
            memo[targetsum]=res
            return res
    memo[targetsum]=None
    return None
print(how_sum_dp(280,[6,14]))