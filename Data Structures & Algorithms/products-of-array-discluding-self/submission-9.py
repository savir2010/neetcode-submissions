class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zro = 0
        output = [0] * len(nums)
        
        for i in nums:
            if i != 0:
                product *= i
            else:
                zro += 1
            
        if zro > 1:
            return output

        for i in range(len(nums)):
            if nums[i] == 0:
                output[i] = product
            else:
                if not zro:
                    output[i]= (product//nums[i])
        
        return output