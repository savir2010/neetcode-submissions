class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) -1 
        best = 0
        while p2 > p1:
            area = min(heights[p1],heights[p2]) * (abs(p2 - p1))
            best = max(area,best)
            # print(area,heights[p1],heights[p2],best)
            if heights[p1] < heights[p2]:
                p1 += 1
            elif heights[p1] >= heights[p2]:
                p2 -=1
            else:
                p1 += 1
                p2 -=1
        return best
        
        