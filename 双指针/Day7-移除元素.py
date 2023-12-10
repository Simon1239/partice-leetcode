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
    
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right-1]
                right -= 1
            else:
                left += 1
        return left, nums[:left]
    
if __name__ == '__main__':
    # nums = [3, 2, 2, 3]
    # nums = [0,1,2,2,3,0,4,2]
    nums = [1,2,3,4,5]
    # val = 3
    # val = 2
    val = 1
    S =Solution()
    print(S.removeElement(nums, val))