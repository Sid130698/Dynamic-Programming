def fib(n):
    if n==0:return 0
    elif n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


print(fib(18))
print(fib(29))
print(fib(7))
#................................................. Dynamic Approach............................#


#using memoization using dictionary in python where key would be the argument and value will be return value

def fib_dp(n,memo={}):
    if n in memo: return memo[n]
    elif n<=2: return 1
    memo[n]=fib_dp(n-1,memo)+fib_dp(n-2,memo)
    return memo[n]
        
print(fib_dp(50))
