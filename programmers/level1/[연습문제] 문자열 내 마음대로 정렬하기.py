# [연습문제] 문자열 내 마음대로 정렬하기
def solution(strings, n):
    strings.sort()
    strings.sort(key=lambda x: x[n])
    return strings
    
if __name__ == "__main__":
    print(solution(["sun", "bed", "car"], 1) == ["car", "bed", "sun"])
    print(solution(["abce", "abcd", "cdx"], 2) == ["abcd", "abce", "cdx"])