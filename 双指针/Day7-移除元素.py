# coding:utf-8

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left = 0
        for right in range(n):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left, nums[:left]
    
if __name__ == '__main__':
    # nums = [3, 2, 2, 3]
    nums = [0,1,2,2,3,0,4,2]
    # val = 3
    val = 2
    S =Solution()
    print(S.removeElement(nums, val))