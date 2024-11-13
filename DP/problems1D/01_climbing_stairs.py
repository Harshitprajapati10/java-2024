# CLIMBING STAIRS
# jump 1 or 2 step at a time ,return number of ways to climb the top

# To return (n+1)th term of fibonacci sequence
# Leetcode 70

def fib(n, memo = None):
    if(memo is None): memo = {}
    if(n in memo): return memo[n]
    if(n<2):return n
    memo[n] =  fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

def climbingStairs(n):
    return fib(n+1);

print(climbingStairs(0))
print(climbingStairs(1))
print(climbingStairs(2))
print(climbingStairs(3))
print(climbingStairs(4))
print(climbingStairs(5))