import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in range(len(points)):
            x,y = points[i]
            dst = ((x**2 + y**2))**0.5
            distances.append((dst,i))
        # print(distances)
        output = []
        heapq.heapify(distances)
        for i in range(k):
            point_idx = heapq.heappop(distances)[1]
            output.append(points[point_idx])
        return output