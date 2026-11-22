class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = {}
        # print(enumerate(nums[0]))
        for i,n in enumerate(nums):
            A[n] = i
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in A:
                if A[diff] != i:
                    return [i,A[diff]]

        