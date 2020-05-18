# [탐욕법(Greedy)] 구명보트
def solution(people, limit):
    from collections import deque
    deq_srt_pp = deque(sorted(people))
    ans = 0
    while deq_srt_pp:
        ans += 1
        usage = deq_srt_pp.pop()
        if deq_srt_pp and usage + deq_srt_pp[0] <= limit:
            deq_srt_pp.popleft()
    return ans

if __name__ == "__main__":
    # print(solution([70, 50, 80, 50], 100))
    # print(solution([70, 50, 80, 50], 100) == 3)
    # print(solution([70, 80, 50], 100))
    # print(solution([70, 80, 50], 100) == 3)
    print(solution([30,30,40, 80, 50], 100))