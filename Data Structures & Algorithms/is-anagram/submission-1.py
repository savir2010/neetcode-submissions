class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct_s = {}
        dct_t = {}
        for x in s:
            if x in dct_s:
                dct_s[x] +=1
            else:
                dct_s[x] = 1
        for x in t:
            if x in dct_t:
                dct_t[x] +=1
            else:
                dct_t[x] = 1
                               
        return dct_s == dct_t
        