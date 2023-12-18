# coding:utf-8

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        cur_sum = 0
        min_sum = float('inf')

        for i in range(n):
            cur_sum += gas[i] - cost[i]
            min_sum = min(min_sum, cur_sum)

        if cur_sum < 0: return -1
        if min_sum >= 0: return 0

        for j in range(n-1, 0, -1):
            min_sum += gas[j] - cost[j]
            if min_sum >= 0:
                return j
            
        return -1
    
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        curSum = 0
        totalSum = 0

        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            totalSum += gas[i] - cost[i]
            if curSum < 0:
                curSum = 0
                start = i + 1
        if totalSum < 0: return -1
        return start
    
if __name__ == '__main__':
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    S = Solution()
    print(S.canCompleteCircuit(gas, cost))