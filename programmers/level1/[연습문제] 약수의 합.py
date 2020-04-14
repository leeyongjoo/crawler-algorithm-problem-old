# [연습문제] 약수의 합
def solution(n):
    aliquot_sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            aliquot_sum += i
    return aliquot_sum

# 다른 풀이
def solution(n):
    return n + sum([i for i in range(1, n // 2 + 1) if n % i == 0])

if __name__ == "__main__":
    print(solution(12) == 28)
    print(solution(5) == 6)
