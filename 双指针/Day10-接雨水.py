# coding:utf-8 

from typing import List

class Solution:
    '''
    动态规划
    '''
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        leftMax = [height[0]] + [0]*(n-1)
        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1], height[i])

        rightMax = [0]*(n-1) + [height[n-1]]
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])

        ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        return ans
    
class Solution:
    '''
    单调栈
    '''
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = list()
        n = len(height)

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i)
        
        return ans

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1

        return ans

if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # height = [4,2,0,3,2,5]
    S = Solution()
    print(S.trap(height))