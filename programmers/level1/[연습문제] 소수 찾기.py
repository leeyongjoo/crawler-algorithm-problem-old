# [연습문제] 소수 찾기
def solution(n):
    # 에라토스테네스의 체
    prime_arr = [False, False] + [True] * (n-1)
    for i in range(2, n+1):
        if prime_arr[i]:
            for j in range(i*2, n+1, i):
                prime_arr[j] = False
    return len([_ for _ in prime_arr if _])

if __name__ == "__main__":
    print(solution(10) == 4)
    print(solution(5) == 3)