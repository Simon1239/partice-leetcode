# coding:utf-8

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next

def printNode(head):
    if head is None:
        return
    cur = head
    while cur:
        print(cur.val, end='->')
        cur = cur.next
    

if __name__ == '__main__':
    nums = [1,2,3,4,5]
    head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    S = Solution()
    res = S.removeNthFromEnd(head,2)
    print(printNode(res))
