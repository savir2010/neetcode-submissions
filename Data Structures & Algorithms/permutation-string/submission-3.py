class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        p1 = 0
        p2 = len(s1) - 1
        window = p2-p1
        freq = {}
        for i in s1:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1
        dct_copy = freq.copy()
        while p2 <= len(s2):
            window_s2 = s2[p1:p2+1]
            for j in window_s2:
                if j in freq:
                    freq[j] -=1
                else:
                    break
                # print(freq)
            all_zeros = all(value == 0 for value in freq.values())
            freq = dct_copy.copy()
            if all_zeros:
                return True

            p1 +=1
            p2 +=1
            # print(window_s2)
        return False