# [스택큐] 프린터
def solution(priorities, location):
    from collections import deque
    import heapq
    deque1 = deque([(p, i) for i, p in enumerate(priorities)])
    heap1 = [-p for p in priorities]
    heapq.heapify(heap1)

    seq = 0
    while deque1 or heap1:
        max_priority = heapq.heappop(heap1)
        p = deque1.popleft()
        if p[0] == -max_priority:
            seq += 1
            if p[1] == location:
                return seq
        else:
            heapq.heappush(heap1, max_priority)
            deque1.append(p)
    return -1

    
if __name__ == "__main__":
    print(solution([2, 1, 3, 2], 2))
    print(solution([2, 1, 3, 2], 2) == 1)
    print(solution([1, 1, 9, 1, 1, 1], 0))
    print(solution([1, 1, 9, 1, 1, 1], 0) == 5)