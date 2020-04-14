# [연습문제] 하샤드 수
def solution(x):
    sum_digit = sum([int(a) for a in str(x)])
    return x % sum_digit == 0
    
if __name__ == "__main__":
    print(solution(10))
    print(solution(10) == True)
    print(solution(12))
    print(solution(12) == True)
    print(solution(11))
    print(solution(11) == False)
    print(solution(13))
    print(solution(13) == False)