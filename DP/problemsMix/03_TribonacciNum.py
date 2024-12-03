# LC 1137 -> nth tribonacci number

# T0   T1    T2   T3    T4   T5  T6   T7
# 0     1     1    2     4   7    13   24

class Solution:
    def tribonacci(self,n):
        def rec(n, memo = None):
            if memo is None: memo = {}
            if n in memo: return memo[n]
            if n <= 1: return n
            if n == 2: return 1
            memo[n] = rec(n-1, memo) + rec(n-2, memo) + rec(n-3, memo)
            return memo[n]
        return rec(n)


obj = Solution()
print(obj.tribonacci(6))
print(obj.tribonacci(7))
print(obj.tribonacci(25))
print(obj.tribonacci(50))