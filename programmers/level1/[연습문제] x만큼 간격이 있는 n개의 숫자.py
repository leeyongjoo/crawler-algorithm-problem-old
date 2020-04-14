# [연습문제] x만큼 간격이 있는 n개의 숫자
def solution(x, n):
    if x > 0:
        return list(range(x, x * n + 1, x))
    elif x < 0:
        return list(range(x, x * n - 1, x))
    else:
        return [0] * n

# 다른 사람의 풀이
def solution(x, n):
    return [i*x + x for i in range(n)]


if __name__ == "__main__":
    print(solution(2, 5))
    print(solution(2, 5) == [2, 4, 6, 8, 10])
    print(solution(4, 3))
    print(solution(4, 3) == [4, 8, 12])
    print(solution(-4, 2))
    print(solution(-4, 2) == [-4, -8])
    print(solution(0, 4))
