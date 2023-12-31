# coding:utf-8

from typing import List

class Solution:
    def canJump(self, nums:List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i+nums[i])
                if rightmost >= n-1:
                    return True
        return False
    
if __name__ == '__main__':
    nums = [2,3,1,1,4]
    S = Solution()
    print(S.canJump(nums))