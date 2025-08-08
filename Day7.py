class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                if nums[i]<nums[j]:
                    for k in range(j+1,len(nums)):
                        if nums[i]<nums[k]<nums[j]:
                            return True
        return False """ 
        stack = []
        third = float('-inf')
        for num in reversed(nums):
            if num < third:
                return True
            while stack and num > stack[-1]:
                third = stack.pop()
            stack.append(num)
        return False 
    
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        no=ListNode(0,head)
        prev=no
        for _ in range(left-1):
            prev=prev.next
        current=prev.next
        for _ in range(right-left):
            next_node=current.next
            current.next,next_node.next,prev.next=next_node.next,prev.next,next_node
        return no.next  
    
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        """if len(nums)>=1:
            k1=[]
            for i in range(len(nums)-k+1):
                num=nums[i:i+k]
                k1.append(max(num))
            return k1"""
        from collections import deque
        q=deque()
        res=[]
        for i ,cur in enumerate(nums):
            while q and nums[q[-1]]<=cur:
                q.pop()
            q.append(i)
            if q[0]==i-k:
                q.popleft()
            if i>=k-1:
                res.append(nums[q[0]])
        return res
        

