class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=[]
        """count=0
        for x in s:
            if x not in l:
                count+=1
                l.append(x)
            else:
                break
        return count 
        for x in range(len(s)):
            for j in range(x+1,len(s)+1):
                l.append(s[x:j])
        count=0        
        for x in l:
            str=[]
            longest=True
            for i in x:
                if i in str:
                    longest=False
                    break
                else:
                    str.append(i)
            if longest:
                count=max((count),len(str))          
        return count """  
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        return maxLength 
    
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        s=0
        e=len(numbers)-1
        while s<=e:
            if numbers[s]+numbers[e]==target:
                return [s+1,e+1]
            elif numbers[s]+numbers[e]<target:
                s+=1
            else:
                e-=1 

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if (nums[i]>=target):
                return i
        return len(nums)        
    """    s=0
        e=len(nums)-1
        if target in nums:
            while(s<=e):
                mid=(s+e)//2
                if nums[mid]==target:
                    return (s+e)//2
                elif nums[mid]>target:
                    e=mid
                else:
                    s=mid
        else:
            i=0
            j=len(nums)-1
            if target<nums[0]:
                return 0
            elif target>nums[-1]:
                return len(nums)+1
            else:
                while i<=j:
                    mid1=nums[i]+nums[j]//2
                    if mid1>target:
                        e=(i+j)//2
                    elif mid1<target:
                        s=(i+j)//2
                    else:
                        return [(i+j)//2]+1 """                     