# coding:utf-8

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 1
        p2 = 1
        count = 0
        while p2 < len(nums):
            if nums[p2] == nums[p1-1]:
                if count == 0:
                    if p2-p1 > 0:
                        nums[p1] = nums[p2]
                    p1 += 1
                count += 1
            else:
                nums[p1] = nums[p2]
                count = 0
                p1 += 1
            p2 += 1
        print(nums)
        return p1
    
if __name__ == '__main__':
    nums = [0,0,1,1,1,1,1,2,3,3]
    S =Solution()
    print(S.removeDuplicates(nums))
