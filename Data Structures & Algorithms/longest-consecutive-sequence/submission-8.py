class Solution:
    import heapq
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        heapq.heapify(nums)
        popq = heapq.heappop(nums)
        best = 1
        consect = 1
        for i in range(len(nums)):
            # print(consect,best,nums,popq)
            pop = heapq.heappop(nums)
            if pop == (int(popq) +1):
                popq = pop
                consect +=1
            elif pop != popq:
                if consect > best:
                    best = consect
                popq = pop
                consect = 1

        if consect > best:
            best = consect   
        return best