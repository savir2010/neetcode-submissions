import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        output = []
        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1

        freq_lst = list(frequency.items())
        freq_list = [(-n[1],n[0]) for n in freq_lst]
        heapq.heapify(freq_list)
        for i in range(k):
            key = heapq.heappop(freq_list)
            key = key[1]
            output.append(key)
        
        return output



