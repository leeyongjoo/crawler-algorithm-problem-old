# [연습문제] 정수 제곱근 판별
def solution(n):
    sr = n ** 0.5   #  square root
    if sr == int(sr):
        return (sr + 1) ** 2
    return -1

if __name__ == "__main__":
    print(solution(121) == 144)
    print(solution(3) == -1)
