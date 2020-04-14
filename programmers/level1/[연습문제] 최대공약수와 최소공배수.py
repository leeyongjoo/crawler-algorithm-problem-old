# [연습문제] 최대공약수와 최소공배수
def solution(n, m):
    cd = [a for a in range(1, min(n, m)+1) if n % a == 0 and m % a == 0]
    cm = [b for b in range(n * m, 0, -1) if b % n == 0 and b % m == 0]
    return [max(cd), min(cm)]

# 다른 사람의 풀이 : 유클리드 호제법
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer


if __name__ == "__main__":
    print(solution(3, 12))
    print(solution(3, 12) == [3, 12])
    print(solution(2, 5))
    print(solution(2, 5) == [1, 10])
