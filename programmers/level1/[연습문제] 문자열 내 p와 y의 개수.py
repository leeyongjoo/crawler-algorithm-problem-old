# [연습문제] 문자열 내 p와 y의 개수
def solution(s):
    s_lower = s.lower()
    return s_lower.count('p') == s_lower.count('y')
    
if __name__ == "__main__":
    print(solution("pPoooyY") == True)
    print(solution("Pyy") == False)