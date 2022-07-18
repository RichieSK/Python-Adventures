# Problem:
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# Thoughts:

# Understanding the Problem:
# Let's take a test example to make sure we understand the problem. Suppose we have [1,2,5] as coins and we need to make up amount = 11.
# So, now there are multiple ways to make up 11. Since, we have infinite repeating of coins, [2,2,2,2,2,1], [5,5,1] and [5,2,2,2] are all valid
# and they aren't exhaustive.
# The challenge is to make sure to find the FEWEST number of coins that make up the sum. This would be -1 if the sum cannot be made.
# For example, if the coins were [4, 5] and we had to make amount = 6, there's no way to make this sum.

# Solution Ideas:
# 1. We know for a fact that if we are given a coin set, and the amount is a coin, the answer would be 1, since the set with fewest number of coins would
# only include the coin. For example, if we have [3,5,6], and amount = 6, the smallest set would be [6]. Similar logic can be applied for 3 and 5.
# 2. Now, here's another idea. To take a sum of n coins, we need not check any coins larger than n. So, let's sort the coins and only use the coins less than n.
# 3. We can create a hashmap that stores the pair of n and minimum number of coins needed to reach n. This can be initialized with the n as the coins as mentioned
# in step (1).
# 4. For the coin set of [c1, c2,...ck] and the amount n, the set with the fewest coins to make up the sum will be
# min(coinChange(n-c1), coinChange(n-c2),...coinChange(n-ck)), up to ck, where ck < n.

# Therefore, this can be solved with dynamic programming using the knowledge we gained from the above 4 steps.
class Solution:
    def coinChange(self, coins: List[int], amount: int, minCoins = None) -> int:
        if minCoins is None:
            coins.sort()
            minCoins = {}
            minCoins[0] = 0
            for coin in coins:
                minCoins[coin] = 1
        try:
            return minCoins[amount]
        except:
            minWaysToAmount = None
            for coin in coins:
                if coin <= 0:
                    continue
                if coin > amount:
                    break
                coinsRequired = self.coinChange(coins, amount-coin, minCoins) + 1
                if coinsRequired > 0 and (minWaysToAmount is None or coinsRequired < minWaysToAmount):
                    minWaysToAmount = coinsRequired
            if minWaysToAmount is None:
                minCoins[amount] = -1
            else:
                minCoins[amount] = minWaysToAmount
            return minCoins[amount]
            
            
