# [힙(Heap)] 더 맵게
def solution(scoville, K):
    import heapq
    heap1 = scoville[:]
    heapq.heapify(heap1)
    mix_count = 0
    if heap1[0] >= K:
            return mix_count
    while len(heap1) > 1:   # len() -> O(1)
        mix_count += 1
        h1 = heapq.heappop(heap1)
        h2 = heapq.heappop(heap1)
        heapq.heappush(heap1, h1 + (h2 * 2))
        if heap1[0] >= K:
            return mix_count
    return -1

if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12], 7))
    print(solution([1, 2, 3, 9, 10, 12], 7) == 2)