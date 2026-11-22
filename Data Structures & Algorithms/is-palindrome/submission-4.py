class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(c for c in s.lower().strip() if c.isalnum())
        p2 = len(cleaned) -1
        p1 = 0
        if len(cleaned) <= 1:
            return True
        while cleaned[p1] == cleaned[p2]:
            p1 += 1
            p2 -=1 
            print(cleaned[p1],cleaned)
            if (abs(p2-p1) <= 1) and cleaned[p1] == cleaned[p2]:
                return True
        return False
