# [연습문제] 문자열 내림차순으로 배치하기
def solution(s):
    return ''.join(sorted(s, reverse=True))
    
if __name__ == "__main__":
    print(solution("Zbcdefg") == "gfedcbZ")