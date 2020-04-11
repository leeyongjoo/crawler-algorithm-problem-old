# [연습문제] 가운데 글자 가져오기
def solution(s):
    s_len = len(s)
    if s_len % 2 == 1:
        return s[int(s_len/2)]
    else:
        return s[int(s_len/2)-1:int(s_len/2)+1]
    
if __name__ == "__main__":
    print(solution("abcde") == "c")
    print(solution("qwer") == "we")