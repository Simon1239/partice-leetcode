# coding:utf-8

from typing import List

class Solution:
    def jump(self, nums:List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n-1):
            if maxPos >= i:
                maxPos = max(maxPos, i+nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
    
if __name__ == '__main__':
    nums = [2,3,1,1,4]
    S = Solution()
    print(S.jump(nums))