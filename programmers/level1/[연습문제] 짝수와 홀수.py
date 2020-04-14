# [연습문제] 짝수와 홀수
def solution(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

#다른 풀이
def solution(num):
    return (num % 2 and "Odd") or "Even"
    
if __name__ == "__main__":
    print(solution(3) == "Odd")
    print(solution(4) == "Even")