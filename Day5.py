class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        return -1
    
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False  

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 0:
            return 0
        left = [0] * n
        right = [0] * n
        max_left = 0
        for i in range(n):
            max_left = max(max_left, height[i])
            left[i] = max_left
        max_right = 0
        for i in reversed(range(n)):
            max_right = max(max_right, height[i])
            right[i] = max_right
        water = 0
        for i in range(n):
            water += min(left[i], right[i]) - height[i]
        return water        