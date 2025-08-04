#Valid Anagram
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        # if len(s)==len(t):
        #     l=[]
        #     for x in s:
        #         if x in t:
        #            l.append(x)
        #         else:
        #             l.append('False')
        #     if 'False' in l:
        #         return False
        #     else:
        #         return True
        # else:
        #     return False    
        #If the string is of the form: str=ssacspd
        #Then Counter(str) does strore it like:
        #{'s':3,'a',:1,'p':1,'d':1}

        # if len(s)!=len(t):
        #     return False
        # return Counter(s)==Counter(t)

        # if len(s)!=len(t):
        #     return False
        # def check(str):
        #     dict1={}
        #     for x in str:
        #         if x not in dict1:
        #             dict1[x]=1
        #         else:
        #             dict1[x]+=1
        #     return dict1
        # return check(s)==check(t)
        return sorted(s)==sorted(t)

#28. Find the Index of the First Occurrence in a String
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle)<=len(haystack):
            if needle in haystack:
                return haystack.find(needle)
            else:
                return -1
        else:
            return -1            

 #Grouping Anagrams
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
    
        from collections import defaultdict
        dict1=defaultdict(list)
        for word in strs:
            key="".join(sorted(word))
            dict1[key].append(word)
        return list(dict1.values())            