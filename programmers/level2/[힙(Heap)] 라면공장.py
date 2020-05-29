# [힙(Heap)] 라면공장
def solution(stock, dates, supplies, k):
    import heapq
    from collections import deque
    ans = 0
    ds_deq = deque(zip(dates, supplies))
    day = stock
    heap = []
    while day < k:
        for i in range(len(ds_deq)):
            if ds_deq[0][0] <= day:
                heapq.heappush(heap, -ds_deq.popleft()[1])
            else:
                break
        day += -heapq.heappop(heap)
        ans += 1
    return ans


if __name__ == "__main__":
    print(solution(4, [4, 10, 15], [20, 5, 10], 30))
    print(solution(4, [4, 10, 15], [20, 5, 10], 30) == 2)
