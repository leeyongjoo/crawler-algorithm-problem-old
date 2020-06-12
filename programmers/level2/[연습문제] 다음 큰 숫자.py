# [연습문제] 다음 큰 숫자
def solution(n):
    count_1 = bin(n)[2:].count('1')
    for i in range(n+1, 1000000):
        if bin(i)[2:].count('1') == count_1:
            return i
    return -1
    
if __name__ == "__main__":
    print(solution(78))
    print(solution(78) == 83)
    print(solution(15))
    print(solution(15) == 23)