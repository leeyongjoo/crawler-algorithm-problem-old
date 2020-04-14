# [연습문제] 핸드폰 번호 가리기
def solution(phone_number):
    return '*'*(len(phone_number)-4) + phone_number[-4:]
    
if __name__ == "__main__":
    print(solution("01033334444"))
    print(solution("01033334444") == "*******4444")
    print(solution("027778888"))
    print(solution("027778888") == "*****8888")