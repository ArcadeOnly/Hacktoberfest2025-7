import heapq

def medianSlidingWindow(nums, k):
    small, large = [], []
    def rebalance():
        while len(small) > len(large) + 1:
            heapq.heappush(large, -heapq.heappop(small))
        while len(large) > len(small):
            heapq.heappush(small, -heapq.heappop(large))
    def get_median():
        return float(-small[0]) if k%2 else (-small[0]+large[0])/2.0

    res = []
    for i, num in enumerate(nums):
        heapq.heappush(small, -num)
        heapq.heappush(large, -heapq.heappop(small))
        rebalance()
        if i >= k-1:
            res.append(get_median())
            out_num = nums[i-k+1]
            if out_num <= -small[0]:
                small.remove(-out_num)
                heapq.heapify(small)
            else:
                large.remove(out_num)
                heapq.heapify(large)
            rebalance()
    return res
