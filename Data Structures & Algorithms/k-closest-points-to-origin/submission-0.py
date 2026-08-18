import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for i in points:
            x,y=i[0],i[1]
            d=(x)**2+(y)**2
            heapq.heappush(heap,(-d,x,y))

        while len(heap)>k:
            heapq.heappop(heap)

        return [[x,y] for (d,x,y) in heap]

