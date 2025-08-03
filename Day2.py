#LC 121
Optimal 
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit



prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices)) 

#LC 125
My sol:
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for x in s:
            if x.isalphanum():
                str=''.join(x.lower())
        return str==s     
s="A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))
Optimum sol:
class Solution(object):
    def isPalindrome(self, s):
        cleaned = []               
        for x in s:
            if x.isalnum():        
              cleaned.append(x.lower())
        cleaned_str = ''.join(cleaned)
        return cleaned_str == cleaned_str[::-1]

s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))

#LC 238
My sol:-
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        pro=1
        for x in range(nums[:x]+nums[x+1:]):
            l.append(pro*nums[x])
        return l    
nums=   [1,2,3,4]    
print(Solution().productExceptSelf(nums))
Optimal:
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]"""
        n = len(nums)
        l = [1] * n
        pro = 1
        for i in range(n):
            l[i] = pro
            pro *= nums[i]
        pro = 1
        for i in range(n - 1, -1, -1):
            l[i] *= pro
            pro *= nums[i]
        return l
  
nums=   [1,2,3,4]    
print(Solution().productExceptSelf(nums))