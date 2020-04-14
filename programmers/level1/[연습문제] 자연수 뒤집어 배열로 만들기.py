# [연습문제] 자연수 뒤집어 배열로 만들기
def solution(n):
    reversed_digit = []
    while n:
        reversed_digit.append(n % 10)
        n //= 10
    return reversed_digit

# 재귀
def solution(n):
    if n < 10:
        return [n]
    return [n % 10] + solution(n // 10)
    
if __name__ == "__main__":
    print(solution(12345) == [5,4,3,2,1])
    print(solution(12345))