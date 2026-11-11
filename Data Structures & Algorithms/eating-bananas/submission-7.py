class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate_hrs(piles,rate):
            hrs = 0
            for x in piles:
                if x % rate != 0:
                    hrs += (x//rate + 1)
                else:
                    hrs += x//rate
            return hrs
        
        max_k = 0
        for x in piles:
            max_k = max(max_k,x)
        # print(max_k)
        start = 1
        end = max_k
        mid = ((max_k + start)//2)
        best = max_k
        while start <= end:
            print(start,mid,end,best)
            hours = calculate_hrs(piles,mid)
            if hours <= h:
                # print('here',best)
                best = min(best,mid)
                end = mid -1
                
            else:
                start = mid +1
            mid = ((end + start)//2)
            # print(hours)
        return best