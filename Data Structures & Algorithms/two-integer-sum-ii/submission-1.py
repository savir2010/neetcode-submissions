class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p2 = len(numbers)-1
        p1=0
        while p1 != p2:
            sm = numbers[p1] + numbers[p2]
            if sm > target:
                p2 -=1
            elif sm < target:
                p1 += 1
            else:
                return [p1+1,p2+1]
        