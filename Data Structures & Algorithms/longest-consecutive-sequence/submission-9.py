class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        startDict = defaultdict(list)
        res = {}
        if not nums:
            return 0


        for num in nums:
            if (num - 1 not in numSet) & (num not in startDict):
                startDict[num].append(num)

        print(startDict)
        greatest_len = 1 
        greatest_key = 1

        for key in startDict:
            i = key
            while i + 1 in numSet:
                startDict[key].append(i + 1)
                i+=1
            if (len(startDict[key]) > greatest_len):
                greatest_key = key
                greatest_len = len(startDict[key])
        
        return greatest_len

        

