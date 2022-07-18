# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Thoughts: This is a dynamic programming solution. We can break down the problem of climbStairs(n) to the sum of climbStairs(n-1) and climbStairs(n-2).
# The reason is that there are two ways to reach n, either from n-1 or n-2.
# Therefore, it is the number of ways in which we can reach n-1 summed with the number of ways in which we can reach n-2.
# We can recursively break this problem until we reach the base case of 1 and 2. There is only 1 way to reach 1, and there are 2 ways to reach 2(1+1 & 2).

# Solution:


class Solution:
    # Top-down approach (memoization)
    # Time Complexity: O(n)
    # Space Complexity: O(n) -> n(Call Stack) + n(Hashmap/List)
    def climbStairs(self, n: int, stairsteps = {}) -> int:
        if stairsteps == {}:
            stairsteps[1] = 1
            stairsteps[2] = 2
        try:
            return stairsteps[n]
        except:
            stairsteps[n] = self.climbStairs(n-1, stairsteps) + self.climbStairs(n-2, stairsteps)
        return stairsteps[n]
    
    # Bottom-up approach (tabulation)
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def climbStairs(self, n: int) -> int:
        stairPaths = [1, 2]
        for i in range(2, n):
            stairPaths.append(stairPaths[i-1] + stairPaths[i-2])
        return stairPaths[n-1]
    
    # Bottom-up approach (tabulation)
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # Initializing ways to 1st step and ways to 2nd step
        waysToNMinusOne, waysToNMinusTwo = 1, 2
        for i in range(2, n):
            waysToN = waysToNMinusOne + waysToNMinusTwo
            # The following is prepping ways to i-1th step & ways to i-2th step for the next iteration
            waysToNMinusOne, waysToNMinusTwo = waysToNMinusTwo, waysToN
        return waysToN
    
