class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ln = len(nums)
        output = []
        for i in range(ln - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = ln - 1
            while j < k:
                sm = nums[i] + nums[j] + nums[k]
                if sm == 0:
                    output.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif sm < 0:
                    j += 1
                else:
                    k -= 1
        return output