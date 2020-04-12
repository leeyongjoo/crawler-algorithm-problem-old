# [연습문제] 문자열 다루기 기본
def solution(s):
    return len(s) in [4,6] and s.isdigit()
    
if __name__ == "__main__":
    print(solution("a234") == False)
    print(solution("1234") == True)