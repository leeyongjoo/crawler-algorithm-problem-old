# [연습문제] 콜라츠 추측
def solution(num):
    run_count = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        run_count += 1

        if run_count == 500:
            return -1
    return run_count

# 다른 풀이(재귀)
# def solution(num):
#     if num == 1:
#         return 0
#
#     if num % 2 == 0:
#         return solution(num / 2) + 1
#     else:
#         return solution(num * 3 + 1) + 1
    
if __name__ == "__main__":
    print(solution(6))
    print(solution(6) == 8)
    print(solution(16))
    print(solution(16) == 4)
    print(solution(626331))
    print(solution(626331) == -1)