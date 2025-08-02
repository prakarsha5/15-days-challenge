#Two sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]            
nums = [2,7,11,15]
target = 9
sol=Solution()
print(sol.twoSum(nums, target))

#Max sum of an subarray
#mysol:
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum=float('-inf')
        if len(nums)==1:
            return nums[0] 
        else:
                for i in range(len(nums)):
                    for j in range(i+1,len(nums)+1):
                        csum=sum(nums[i:j])
                        if csum>maxsum:
                            maxsum=csum 
                return(maxsum)
nums = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution()
print(sol.maxSubArray(nums)) 
#optimum
class Solution(object):
    def maxSubArray(self, nums):
        max_current = max_global = nums[0]
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current + nums[i])
            max_global = max(max_global, max_current)
        return max_global
    
#removeDuplicates
# my sol
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=set(nums)
        numl=sorted(num)
        for x in range(len(nums)-len(numl)):
            numl.append('_')
        print(numl) 
nums=[1,1,2]  
sol=Solution() 
print(sol.removeDuplicates(nums)) 
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        i = 0 
        for j in range(1, len(nums)): 
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1    
