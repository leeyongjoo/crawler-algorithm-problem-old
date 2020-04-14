# [연습문제] 자릿수 더하기
def solution(n):
    sum_digit = 0
    while n:
        sum_digit += n%10
        n //= 10
    return sum_digit
    
if __name__ == "__main__":
    n = 123
    print(solution(n) == 6)
    print(solution(987) == 24)