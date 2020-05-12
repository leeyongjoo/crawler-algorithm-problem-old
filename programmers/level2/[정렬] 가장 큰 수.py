# [정렬] 가장 큰 수
def solution(numbers):
    import heapq
    heapq._heapify_max(numbers)
    if numbers[0] == 0:
        return '0'
    max_len = len(str(numbers[0]))

    li = list(map(str, numbers))
    li.sort(key=lambda a: a * (max_len - len(a) + 1), reverse=True)
    return ''.join(li)

# 다른 사람의 풀이
import functools

def comparator(a, b):
    t1 = a + b
    t2 = b + a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))  # t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    return str(int(''.join(n)))

if __name__ == "__main__":
    print(solution([6, 10, 2]))
    print(solution([6, 10, 2]) == "6210")
    print(solution([3, 30, 34, 5, 9]))
    print(solution([3, 30, 34, 5, 9]) == "9534330")
    print(solution([22222222, 22222220, 2, ]))
