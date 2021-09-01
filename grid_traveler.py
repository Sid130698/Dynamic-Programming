''' say that you are a traveler on a 2D grid. Yout begin in the top-left corner
    and your goal is to travel to the bottom-right corner.
    You may only move down or right

    In how many ways can you travel to the goal on a grid with dimensions m*n?

    '''
#....................... Brute Force direct approach recursive.............................#
#time complexity O(2^(n+m))

def grid_traveler(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveler(m-1, n)+grid_traveler(m, n-1)


print(grid_traveler(1, 1))
print(grid_traveler(2, 3))
print(grid_traveler(3, 2))



#............................Dynamic Programming Approach....................................#
#time  complexity is O(m*n)
def grid_traveler_dp(m, n, memo={}):
    key = str(m) + ',' + str(n)

    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key]=grid_traveler_dp(m-1, n,memo)+grid_traveler_dp(m, n-1,memo)
    return memo[key]


print(grid_traveler_dp(18, 18))