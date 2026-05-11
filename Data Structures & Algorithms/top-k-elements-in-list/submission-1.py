class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countdict = {}
        for num in nums:
            countdict[num] = countdict.get(num, 0) + 1

        heap = []

        for num, count in countdict.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)


        return [heapq.heappop(heap)[1] for _ in range(k)]