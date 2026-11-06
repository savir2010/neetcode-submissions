class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) -1
        mid = (start + end)//2

        while end-start > 1:
            # print(nums[start],nums[mid],nums[end])
            if (nums[mid] - nums[end]) < 0:
                end = mid
                mid = (start + end)//2
            elif (nums[mid] - nums[start]) > 0:
                start = mid
                mid = (start + end)//2
            
        # print(nums[start],nums[mid],nums[end])
        return min(nums[start],nums[end])
        