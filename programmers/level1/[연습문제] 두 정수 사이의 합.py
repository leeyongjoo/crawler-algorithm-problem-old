# [연습문제] 두 정수 사이의 합
def solution(a, b):
    start, end = min(a,b), max(a,b)
    return sum(range(start,end+1))
    
if __name__ == "__main__":
    print(solution(3, 5) == 12)
    print(solution(3, 3) == 3)
    print(solution(5, 3) == 12)