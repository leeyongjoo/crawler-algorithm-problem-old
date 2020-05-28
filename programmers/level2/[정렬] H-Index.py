# [정렬] H-Index
def solution(citations):
    citations.sort()
    for i in range(len(citations)):
        h = len(citations) - i
        if citations[i] >= h:
            return h
    return 0

if __name__ == "__main__":
    print(solution([3, 0, 6, 1, 5]))
    print(solution([3, 0, 6, 1, 5]) == 3)
