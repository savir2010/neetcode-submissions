class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negated = [-x for x in nums]
        heapq.heapify(negated)

        rcent = 0
        for i in range(k):
            rcent = heapq.heappop(negated)
        
        return -rcent
